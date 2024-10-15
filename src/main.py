from controllers.Controller import Controller
from models.DeviceManager import DeviceManager
from models.Sheet import Sheet
from views.Root import Root
from views.View import View
from views.ViewFacade import ViewFacade


def main():
    sheet = Sheet()
    root = Root()
    view = View(root)
    viewFacade = ViewFacade(view)
    controller = Controller(viewFacade, sheet)
    controller.start()

if __name__ == "__main__":
    main()