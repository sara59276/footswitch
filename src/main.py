from controllers.controller import Controller
from models.data import Data
from models.metadata import Metadata
from views.view_manager import ViewManager
from views.root import Root
from views.view import View


def main():
    metadata = Metadata()
    data = Data()

    root = Root()
    view = View(root)
    facade = ViewManager(view)

    controller = Controller(facade, metadata, data)
    controller.start_app()

if __name__ == "__main__":
    main()