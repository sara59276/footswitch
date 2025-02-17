import os
from tkinter import messagebox

from config.config_manager import ConfigManager
from models.data import Data
from models.metadata import Metadata
from utils.file_utils import FileUtil
from utils.footswitch_monitor import FootswitchMonitor
from utils.string_utils import StringUtils
from utils.time_util import TimeUtil
from views.view_manager import ViewManager


class Presenter:

    ROOT_DIR = os.path.abspath(os.sep)
    DATA_DIR = os.path.join(ROOT_DIR, 'Footswitch', 'data')

    def __init__(
            self,
            view: ViewManager,
            metadata: Metadata,
            data: Data,
    ):
        self.__metadata = metadata
        self.__data = data
        self.__view = view

        self.__footswitch_monitor = FootswitchMonitor()
        self.__filepath = None
        self.__is_footswitch_pressed = False
        self.__has_session_started = False

        self.__current_start_datetime = None
        self.__current_end_datetime = None

        self._bind()

    def start_app(self) -> None:
        self.display_footswitch_connection()
        self.__view.display_footswitch_released_icon()
        self.__footswitch_monitor.start_monitoring(self.on_device_connect, self.on_device_disconnect)
        self.__view.activate_start_button()
        self.__view.deactivate_end_button()
        self.__view.start_mainloop()

    def start_session(self) -> None:
        try:
            self._update_data()

            if self.__filepath:
                self.__view.clear_msg()
                filename = FileUtil.get_filename(self.__filepath)
                folder = FileUtil.get_folder(self.__filepath)
                self.__view.display_success(f"File name: {filename}"
                                            f"\nSaved in folder: {folder}"
                                            f"\n(All changes are automatically saved)")
                self.__view.disable_user_inputs()
                self.__view.deactivate_start_button()
                self.__view.activate_end_button()
                session_start_time = self.__metadata.get_session_start()
                self.__view.display_session_start(session_start_time)
                self.__has_session_started = True

        except (FileExistsError, FileNotFoundError, ValueError) as e:
            self.__view.display_error(f"{e}")
            raise
        except Exception as e:
            self.__view.display_error(f"Unhandled error: {e}")
            raise

    def end_session(self) -> None:
        if self.__filepath:
            self.__metadata.set_session_end(self.__filepath)

            # unoptimal but resolves data header bug, cf. github issue #2
            self.__data.update(self.__filepath, self.__view.get_sheet_content())

        self.__view.deactivate_end_button()
        session_end_time = self.__metadata.get_session_end()
        self.__view.display_session_end(session_end_time)
        self.__has_session_started = False

    def clear_session(self) -> None:
        if self.__view.sheet_contains_empty_events():
            has_cancelled = messagebox.askokcancel(
                "Warning",
                "Empty event(s) detected.\nDo you still want to clear ?",
                icon='warning',
            )
            if not has_cancelled:
                return

        self.end_session()
        self._reset_attributes()
        self.__view.reset_view()
        self.__view.enable_user_inputs()
        self.__view.activate_start_button()

    def display_footswitch_connection(self) -> None:
        is_detected = self.__footswitch_monitor.is_footswitch_connected()
        self.__view.display_footswitch_connected() if is_detected else self.__view.display_footswitch_disconnected()

    def footswitch_pressed(self, event) -> None:
        self.__view.display_footswitch_pressed_icon()

        if self.__has_session_started and not self.__is_footswitch_pressed:
            self.__is_footswitch_pressed = True

            start_time = TimeUtil.get_formatted_current_time()
            self.__view.add_start_time(start_time)
            self.__current_start_datetime = TimeUtil.get_current_date()

            updated_data = self.__view.get_sheet_content()
            self.__data.update(self.__filepath, updated_data)

    def footswitch_released(self, event) -> None:
        self.__view.display_footswitch_released_icon()

        if self.__has_session_started:
            self.__is_footswitch_pressed = False

            end_time = TimeUtil.get_formatted_current_time()
            self.__view.add_end_time(end_time)
            self.__current_end_datetime = TimeUtil.get_current_date()

            mean_time = TimeUtil.get_formatted_midpoint_time(
                self.__current_start_datetime,
                self.__current_end_datetime,
            )
            self.__view.add_mean_time(mean_time)

            updated_data = self.__view.get_sheet_content()
            self.__data.update(self.__filepath, updated_data)
            self.__view.sheet_scroll_down()

    def on_sheet_modified(self, event) -> None:
        data = self.__view.get_sheet_content()
        self.__data.update(self.__filepath, data)

    def on_device_connect(self, device_id, device_info) -> None:
        self.__view.display_footswitch_connected()

    def on_device_disconnect(self, device_id, device_info) -> None:
        self.__view.display_footswitch_disconnected()

    def on_close_window_button(self) -> None:
        if self.__filepath:
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
            StringUtils.is_filename_friendly_character,
            StringUtils.is_letter,
            StringUtils.is_digit,
        )
        self.__view.bind_sheet(
            self.on_sheet_modified,
        )
        self.__view.bind_close_window_button(
            self.on_close_window_button,
        )

    def _initialize_filepath(self, scan_id: str, animal_id: str, experimenter_initials: str):
        self.__filepath = FileUtil.create_file(
            destination_folder=self._get_destination_folder(),
            scan_id=scan_id,
            animal_id=animal_id,
            experimenter_initials=experimenter_initials,
            current_date=TimeUtil.get_formatted_current_date("%Y%m%d"),
        )

    def _get_destination_folder(self) -> str:
        year, month, day = TimeUtil.get_current_year_month_day()
        return os.path.join(Presenter.DATA_DIR, year, month, day)

    def _update_data(self) -> None:
        scan_id, animal_id, experimenter_initials, delay = self.__view.get_user_inputs()
        experimenter_initials = experimenter_initials.upper()

        self._initialize_filepath(scan_id, animal_id, experimenter_initials)

        self.__metadata.set_starting_metadata(
            filepath=self.__filepath,
            scan_id=scan_id,
            animal_id=animal_id,
            experimenter_initials=experimenter_initials,
            delay=delay,
        )
        self.__data.update(
            self.__filepath,
        )
        data = self.__data.get(self.__filepath)
        self.__view.set_sheet(data)

    def _get_footswitch_key(self) -> str:
        config = ConfigManager()
        return config.get("footswitch_key")

    def _reset_attributes(self) -> None:
        if self.__filepath:
            FileUtil.set_readonly(self.__filepath)
            self.__filepath = None

        self.__current_start_datetime = None
        self.__current_end_datetime = None
