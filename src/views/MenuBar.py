from tkinter import Menu


class MenuBar:
    def __init__(self, root, commands):
        super().__init__()

        menubar = Menu(root)

        goto_menu = Menu(menubar, tearoff=False)

        goto_menu.add_command(
            label="Exit",
            command=commands["quit"],
        )
        menubar.add_cascade(label="Go to", menu=goto_menu)

        help_menu = Menu(menubar, tearoff=False)

        help_menu.add_command(
            label="Help",
            command=commands["help"],
        )
        help_menu.add_command(
            label="About",
            command=commands["about"]
        )
        menubar.add_cascade(label="Help", menu=help_menu)

        root.config(menu=menubar)



