import re

from models.DeviceManager import DeviceManager
from models.FileManager import FileManager
from models.DataSheet import DataSheet
from views.ViewFacade import ViewFacade


class Controller:
    def __init__(self, view: ViewFacade, data_sheet: DataSheet):
        self.data_sheet = data_sheet
        self.view = view
        self._bind()

    def start(self) -> None:
        self.display_footswitch_connection()
        DeviceManager.start_monitoring(self.on_device_connect, self.on_device_disconnect)
        self.view.start_mainloop()

    def _bind(self) -> None:
        self.view.bind_widgets(
            self.start_measures,
            self.reset_measures,
        )
        self.view.bind_footswitch(
            self.footswitch_pressed,
            self.footswitch_released,
        )
        self.view.bind_entry_constraints(
            self.validate_experimenter_input,
        )

    def display_footswitch_connection(self) -> None:
        is_detected = DeviceManager.is_footswitch_connected()
        self.view.display_footswitch_connected() if is_detected else self.view.display_footswitch_disconnected()

    def start_measures(self) -> None:
        try:
            self.view.clear_msg()
            scan_id, animal_id, experimenter_initials = self.view.get_user_inputs()
            filepath = FileManager.create_filepath(
                destination_folder=FileManager.get_destination_folder(),
                scan_id=scan_id,
                animal_id=animal_id,
                experimenter_initials=experimenter_initials.upper()
            )
            self.data_sheet.initialize(filepath)
            if filepath:
                self.view.display_success(f"File created : {filepath}")
            else:
                self.view.display_error(f"File not created.")

            self.view.disable_user_inputs()
            self.update_sheet()
        except (FileExistsError, ValueError) as e:
            self.view.display_error(str(e))
        except Exception as e:
            self.view.display_error(str(e))
            raise

    def reset_measures(self) -> None:
        # TODO add dialog "sure to reset ?"
        self.view.reset_view()
        self.data_sheet.reset()
        self.view.enable_user_inputs()

    def footswitch_pressed(self, event) -> None:
        print("Footswitch pressed")


    def footswitch_released(self, event) -> None:
        print("Footswitch released")

    def validate_experimenter_input(self, value):
        pattern = r'^[A-Za-z]+$'
        return bool(re.fullmatch(pattern, value))

    def update_sheet(self) -> None:
        data = self.data_sheet.get_data()
        self.view.update_sheet(data)

    def on_device_connect(self, device_id, device_info) -> None:
        self.view.display_footswitch_connected()

    def on_device_disconnect(self, device_id, device_info) -> None:
        self.view.display_footswitch_disconnected()