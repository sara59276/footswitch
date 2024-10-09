from models.Model import Model
from views.View import View


class MenuBarController:
    def __init__(self, view: View, model: Model):
        self.view = view
        self.model = model

    def quit(self):
        self.view.root.quit()

    def help(self):
        pass

    def about(self):
        pass