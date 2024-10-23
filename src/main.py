from controllers.Controller import Controller
from models.Data import Data
from models.Metadata import Metadata
from views.Facade import Facade
from views.Root import Root
from views.View import View


def main():
    metadata = Metadata()
    data = Data()

    root = Root()
    view = View(root)
    facade = Facade(view)

    controller = Controller(facade, metadata, data)
    controller.start_app()

if __name__ == "__main__":
    main()