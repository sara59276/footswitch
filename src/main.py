from controllers.Controller import Controller
from models.Sheet import Sheet
from views.Root import Root
from views.View import View
from views.ViewFacade import ViewFacade


def main():
    model = Sheet()
    root = Root()
    view = View(root)
    viewFacade = ViewFacade(view)
    controller = Controller(viewFacade, model)
    controller.start()

if __name__ == "__main__":
    main()