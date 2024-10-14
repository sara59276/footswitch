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
        self.view.bind_widgets(self.start_command, self.reset_command)

    def start_command(self):
        try:
            self.model.create_new_file(
                destination_folder=os.path.dirname(os.path.abspath(__file__)),
                scan_id="scan123",
                animal_id="a103000",
            )
        except FileExistsError as e:
            self.view.display_error(e)
        except Exception as e:
            self.view.display_error(e)
            raise

    def reset_command(self):
        pass