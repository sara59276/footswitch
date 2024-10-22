from controllers.Controller import Controller
from models.EventLogSheet import EventLogSheet
from views.Root import Root
from views.View import View
from views.ViewFacade import ViewFacade


def main():
    sheet = EventLogSheet()
    root = Root()
    view = View(root)
    viewFacade = ViewFacade(view)
    controller = Controller(viewFacade, sheet)
    controller.start_app()

if __name__ == "__main__":
    main()