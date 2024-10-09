from controllers.MainController import MainController
from controllers.MenuBarController import MenuBarController
from views.MenuBar import MenuBar


class Controller:
    def __init__(self, view, model):
        self.model = model
        self.view = view

        self.menubar_controller = MenuBarController(view, model)
        self.view.menubar = MenuBar(self.view.root, self._get_menu_commands())

        self.main_controller = MainController(view, model)

    def start(self):
        self.view.switch("main_view")
        self.view.start_mainloop()

    def _get_menu_commands(self):
        return {
            "quit": self.menubar_controller.quit,
            "help": self.menubar_controller.help,
            "about": self.menubar_controller.about,
        }