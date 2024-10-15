from controllers.Controller import Controller
from models.DeviceManager import DeviceManager
from models.Sheet import Sheet
from views.Root import Root
from views.View import View
from views.ViewFacade import ViewFacade


def main():
    sheet = Sheet()
    device_manager = DeviceManager()
    root = Root()
    view = View(root)
    viewFacade = ViewFacade(view)
    controller = Controller(viewFacade, sheet, device_manager)
    controller.start()

if __name__ == "__main__":
    main()