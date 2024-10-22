from controllers.Controller import Controller
from models.SessionData import SessionData
from views.Facade import Facade
from views.Root import Root
from views.View import View


def main():
    session_data = SessionData()
    root = Root()
    view = View(root)
    facade = Facade(view)
    controller = Controller(facade, session_data)
    controller.start_app()

if __name__ == "__main__":
    main()