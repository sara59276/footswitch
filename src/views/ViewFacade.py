class ViewFacade:
    def __init__(self, view):
        self.view = view

    def start_mainloop(self):
        self.view.start_mainloop()

    def bind_buttons(self, start_command, reset_command):
        self.view.start_btn.config(command=start_command)
        self.view.reset_btn.config(command=reset_command)