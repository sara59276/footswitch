from calendar import error


class ViewFacade:
    def __init__(self, view):
        self.view = view

    def start_mainloop(self):
        self.view.start_mainloop()

    def bind_widgets(self, start_command, reset_command):
        self.view.start_btn.config(command=start_command)
        self.view.reset_btn.config(command=reset_command)

    def display_error(self, error_msg):
        self.view.error_value.set(error_msg)