from controllers.Controller import Controller
from models.Model import Model
from views.Root import Root
from views.View import View


def main():
    model = Model()
    root = Root()
    view = View(root)
    controller = Controller(view, model)
    controller.start()

if __name__ == "__main__":
    main()