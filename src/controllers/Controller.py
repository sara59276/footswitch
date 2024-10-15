import os

from models.DeviceManager import DeviceManager
from models.Sheet import Sheet
from views.ViewFacade import ViewFacade


class Controller:
    def __init__(self, view: ViewFacade, sheet: Sheet):
        self.sheet = sheet
        self.view = view
        self._bind()

    def start(self):
        self.detect_device()
        DeviceManager.start_monitoring(self.on_device_connect, self.on_device_disconnect)
        self.view.start_mainloop()

    def _bind(self):
        self.view.bind_widgets(self.start_measures, self.reset_measures)

    def detect_device(self):
        is_detected = DeviceManager.is_footswitch_connected()
        self.view.display_connected_device() if is_detected else self.view.display_disconnected_device()

    def start_measures(self):
        try:
            self.view.clear_error()
            scan_id, animal_id, experimenter_id = self.view.get_user_inputs()
            file_path = self.sheet.create_new_file(
                destination_folder=os.path.dirname(os.path.abspath(__file__)),
                scan_id=scan_id,
                animal_id=animal_id,
            )
            if file_path:
                self.view.display_success(f"File created : {file_path}")
            else:
                self.view.display_error(f"File not created.")

            self.view.disable_user_inputs()
            self.update_sheet()
        except FileExistsError as e:
            self.view.display_error(e)
        except ValueError as e:
            self.view.display_error(e)
        except Exception as e:
            self.view.display_error(e)
            raise

    def reset_measures(self):
        # TODO add dialog "sure to reset ?"
        self.view.reset()
        self.sheet.reset()
        self.view.enable_user_inputs()

    def update_sheet(self):
        data = self.sheet.get_file_content()
        self.view.update_sheet(data)

    def on_measure_completion(self):
        measure_data = self.view.get_last_measure()
        self.sheet.append_measure(measure_data)

    def on_device_connect(self, device_id, device_info):
        self.view.display_connected_device()

    def on_device_disconnect(self, device_id, device_info):
        self.view.display_disconnected_device()