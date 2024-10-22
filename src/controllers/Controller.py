import re
from datetime import datetime

from models.EventLogSheet import EventLogSheet
from models.SessionData import SessionData
from models.static.DeviceManager import DeviceManager
from models.static.FileManager import FileManager
from models.static.TimeManager import TimeManager
from views.ViewFacade import ViewFacade


class Controller:
    def __init__(self, view: ViewFacade, sheet: EventLogSheet):
        self.sheet = sheet
        self.__view = view

        self.__session_data: SessionData = SessionData()
        self.__is_footswitch_pressed = False
        self.__has_started = False

        self._bind()

    def start_app(self) -> None:
        self.display_footswitch_connection()
        self.__view.display_footswitch_released_icon()
        DeviceManager.start_monitoring(self.on_device_connect, self.on_device_disconnect)
        self.__view.start_mainloop()

    def _bind(self) -> None:
        self.__view.bind_buttons(
            self.start_session,
            self.end_session,
            self.clear_session,
        )
        self.__view.bind_footswitch(
            self.footswitch_pressed,
            self.footswitch_released,
        )
        self.__view.bind_entry_constraints(
            self.validate_scan_and_animal_inputs,
            self.validate_experimenter_input,
        )
        self.__view.bind_sheet(
            self.on_sheet_modified,
        )
        self.__view.bind_close_window_button(
            self.on_close_window_button,
        )

    def start_session(self) -> None:
        try:
            self.__view.clear_msg()

            current_date = TimeManager.get_current_date()
            session_start_time = TimeManager.get_current_time()
            scan_id, animal_id, experimenter_initials = self.__view.get_user_inputs()

            self.__session_data = SessionData(
                current_date=current_date,
                session_start=session_start_time,
                scan_id=scan_id,
                animal_id=animal_id,
                experimenter_initials=experimenter_initials,
            )

            filepath = FileManager.create_filepath(
                destination_folder=FileManager.get_destination_folder(),
                scan_id=scan_id,
                animal_id=animal_id,
                experimenter_initials=experimenter_initials.upper(),
                current_date=current_date,
            )

            self.sheet.initialize(filepath)
            if filepath:
                self.__view.display_success(f"File created: {filepath}")
            else:
                self.__view.display_error(f"Error: File not created")

            self.__view.disable_user_inputs()
            self.load_sheet_content()
            self.__has_started = True
        except (FileExistsError, ValueError) as e:
            self.__view.display_error(str(e))
        except Exception as e:
            self.__view.display_error(str(e))
            raise

    def end_session(self) -> None:
        session_end_time = TimeManager.get_current_time()
        self.__session_data.set_session_end(session_end_time)
        # TODO update file

    def clear_session(self) -> None:
        self.sheet.set_readonly()
        self.__view.reset_view()
        self.sheet.reset()
        self.__view.enable_user_inputs()
        self.__has_started = False

    def display_footswitch_connection(self) -> None:
        is_detected = DeviceManager.is_footswitch_connected()
        self.__view.display_footswitch_connected() if is_detected else self.__view.display_footswitch_disconnected()

    def footswitch_pressed(self, event) -> None:
        self.__view.display_footswitch_pressed_icon()

        if self.__has_started and not self.__is_footswitch_pressed:
            self.__is_footswitch_pressed = True
            current_time = TimeManager.get_current_time()
            self.__view.add_start_time(current_time)
            print("Footswitch pressed")

    def footswitch_released(self, event) -> None:
        self.__view.display_footswitch_released_icon()

        if self.__has_started:
            self.__is_footswitch_pressed = False
            current_time = datetime.now().time().strftime("%H:%M:%S.%f")
            self.__view.add_end_time(current_time)
            updated_data_sheet = self.__view.get_sheet_content()
            self.sheet.update(updated_data_sheet)
            self.__view.append_empty_row()
            self.__view.sheet_scroll_down()

            print("Footswitch released")

    def validate_scan_and_animal_inputs(self, value) -> bool:
        pattern = r'^[\w]+$'
        return bool(re.fullmatch(pattern, value))

    def validate_experimenter_input(self, value) -> bool:
        pattern = r'^[A-Za-z]+$'
        return bool(re.fullmatch(pattern, value))

    def on_sheet_modified(self, event) -> None:
        data = self.__view.get_sheet_content()
        self.sheet.update(data)

    def load_sheet_content(self) -> None:
        data = self.sheet.get_data_from_file()
        self.__view.set_sheet(data)

    def on_device_connect(self, device_id, device_info) -> None:
        self.__view.display_footswitch_connected()

    def on_device_disconnect(self, device_id, device_info) -> None:
        self.__view.display_footswitch_disconnected()

    def on_close_window_button(self) -> None:
        self.sheet.set_readonly()
        root = self.__view.get_root()
        root.destroy()
