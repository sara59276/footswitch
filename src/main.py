from controllers.Controller import Controller
from models.Model import Model
from views.View import View


def main():
    model = Model()
    view = View()
    controller = Controller(view, model)
    controller.start()

if __name__ == "__main__":
    main()