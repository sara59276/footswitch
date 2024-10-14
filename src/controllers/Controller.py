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
        pass
    def reset_command(self):
        pass