import os

from models.Sheet import Sheet
from views.ViewFacade import ViewFacade


class Controller:
    def __init__(self, view: ViewFacade, model: Sheet):
        self.model = model
        self.view = view
        self._bind()

    def start(self):
        self.view.start_mainloop()

    def _bind(self):
        self.view.bind_widgets(self.start_measures, self.reset_measures)

    def start_measures(self):
        try:
            self.view.clear_error()
            scan_id, animal_id, experimenter_id = self.view.get_user_inputs()
            self.model.create_new_file(
                destination_folder=os.path.dirname(os.path.abspath(__file__)),
                scan_id=scan_id,
                animal_id=animal_id,
            )
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
        self.model.reset()
        self.view.enable_user_inputs()

    def update_sheet(self):
        data = self.model.get_file_content()
        self.view.update_sheet(data)

    def on_measure_completion(self):
        measure_data = self.view.get_last_measure()
        self.model.append_measure(measure_data)