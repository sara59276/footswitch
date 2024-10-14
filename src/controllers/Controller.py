class Controller:
    def __init__(self, view, model):
        self.model = model
        self.view = view
        self._bind()

    def start(self):
        self.view.start_mainloop()

    def _bind(self):
        pass
