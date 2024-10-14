from controllers.Controller import Controller
from models.Model import Model
from views.Root import Root
from views.View import View
from views.ViewFacade import ViewFacade


def main():
    model = Model()
    root = Root()
    view = View(root)
    viewFacade = ViewFacade(view)
    controller = Controller(viewFacade, model)
    controller.start()

if __name__ == "__main__":
    main()