from controllers.Controller import Controller
from models.DataSheet import DataSheet
from views.Root import Root
from views.View import View
from views.ViewFacade import ViewFacade


def main():
    sheet = DataSheet()
    root = Root()
    view = View(root)
    viewFacade = ViewFacade(view)
    controller = Controller(viewFacade, sheet)
    controller.start()

if __name__ == "__main__":
    main()