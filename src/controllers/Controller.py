import os


class Controller:
    def __init__(self, view_facade, model):
        self.model = model
        self.view = view_facade
        self._bind()

    def start(self):
        self.view.start_mainloop()

    def _bind(self):
        self.view.bind_buttons(self.start_command, self.reset_command)

    def start_command(self):
        self.model.initialize_sheet(
            destination_folder=os.path.dirname(os.path.abspath(__file__)),
            scan_id="scan123",
            animal_id="a103000",
        )

    def reset_command(self):
        pass