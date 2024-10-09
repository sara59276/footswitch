from models.Model import Model
from views.View import View


class MainController:
    def __init__(self, view: View, model: Model) -> None:
        self.view = view
        self.model = model
        self.frame = self.view.frames["main_view"]
        self._bind()

    def _bind(self):
        pass


