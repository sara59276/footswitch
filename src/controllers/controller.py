import re

from models.data import Data
from models.metadata import Metadata
from config.config_manager import ConfigManager
from utils.file_utils import FileUtil
from utils.footswitch_monitor import FootswitchMonitor
from utils.time_util import TimeUtil
from views.facade_interface import FacadeInterface


class Controller:
    def __init__(
            self,
            view: FacadeInterface,
            metadata: Metadata,
            data: Data,
    ):
        self.__metadata = metadata
        self.__data = data
        self.__view = view

        self.__footswitch_monitor = FootswitchMonitor()

        self.__filepath = None
        self.__is_footswitch_pressed = False
        self.__has_started = False

        self._bind()

    def start_app(self) -> None:
        self.display_footswitch_connection()
        self.__view.display_footswitch_released_icon()
        self.__footswitch_monitor.start_monitoring(self.on_device_connect, self.on_device_disconnect)
        self.__view.start_mainloop()

    def start_session(self) -> None:
        try:
            scan_id, animal_id, experimenter_initials = self.__view.get_user_inputs()
            self._initialize_filepath(scan_id, animal_id, experimenter_initials)

            if self.__filepath:
                print("before. filepath = ", self.__filepath)
                self.__view.display_success(f"File created: {self.__filepath}")
                print("after. filepath = ", self.__filepath)
            else:
                raise FileNotFoundError(f"Error: File not created")

            self.__metadata.set_starting_metadata(
                filepath=self.__filepath,
                scan_id=scan_id,
                animal_id=animal_id,
                experimenter_initials=experimenter_initials,
            )
            self.__data.update(
                self.__filepath,
            )

            self.__view.clear_msg()
            self.__view.disable_user_inputs()
            self._load_sheet_content()
            self.__has_started = True

        except (FileExistsError, FileNotFoundError, ValueError) as e:
            self.__view.display_error(str(e))
        except Exception as e:
            self.__view.display_error(str(e))
            raise

    def end_session(self) -> None:
        self.__metadata.set_session_end(self.__filepath)
        FileUtil.set_readonly(self.__filepath)

    def clear_session(self) -> None:
        FileUtil.set_readonly(self.__filepath)
        self.__has_started = False

        self.__view.reset_view()
        self.__view.enable_user_inputs()

    def display_footswitch_connection(self) -> None:
        is_detected = self.__footswitch_monitor.is_footswitch_connected()
        self.__view.display_footswitch_connected() if is_detected else self.__view.display_footswitch_disconnected()

    def footswitch_pressed(self, event) -> None:
        self.__view.display_footswitch_pressed_icon()

        if self.__has_started and not self.__is_footswitch_pressed:
            self.__is_footswitch_pressed = True
            current_time = TimeUtil.get_current_time()
            self.__view.add_start_time(current_time)

    def footswitch_released(self, event) -> None:
        self.__view.display_footswitch_released_icon()

        if self.__has_started:
            self.__is_footswitch_pressed = False

            current_time = TimeUtil.get_current_time()
            self.__view.add_end_time(current_time)

            updated_data = self.__view.get_sheet_content()
            self.__data.update(self.__filepath, updated_data)

            self.__view.append_empty_row()
            self.__view.sheet_scroll_down()

    def validate_scan_and_animal_inputs(self, value) -> bool:
        pattern = r'^[\w]+$'
        return bool(re.fullmatch(pattern, value))

    def validate_experimenter_input(self, value) -> bool:
        pattern = r'^[A-Za-z]+$'
        return bool(re.fullmatch(pattern, value))

    def on_sheet_modified(self, event) -> None:
        data = self.__view.get_sheet_content()
        self.__data.update(self.__filepath, data)

    def on_device_connect(self, device_id, device_info) -> None:
        self.__view.display_footswitch_connected()

    def on_device_disconnect(self, device_id, device_info) -> None:
        self.__view.display_footswitch_disconnected()

    def on_close_window_button(self) -> None:
        FileUtil.set_readonly(self.__filepath)
        root = self.__view.get_root()
        root.destroy()

    def _bind(self) -> None:
        self.__view.bind_buttons(
            self.start_session,
            self.end_session,
            self.clear_session,
        )
        self.__view.bind_footswitch(
            self._get_footswitch_key(),
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

    def _initialize_filepath(self, scan_id: str, animal_id: str, experimenter_initials: str):
        dest_folder = FileUtil.get_destination_folder()
        current_date = TimeUtil.get_current_date()

        self.__filepath = FileUtil.create_filepath(
            destination_folder=dest_folder,
            scan_id=scan_id,
            animal_id=animal_id,
            experimenter_initials=experimenter_initials,
            current_date=current_date,
        )

    def _load_sheet_content(self) -> None:
        data = self.__data.get(self.__filepath)
        self.__view.set_sheet(data)

    def _get_footswitch_key(self) -> str:
        config = ConfigManager()
        return config.get("footswitch_key")