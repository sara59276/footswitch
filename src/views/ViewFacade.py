import tkinter

from views.View import View


class ViewFacade:
    def __init__(self, view: View):
        self.view = view

    def start_mainloop(self):
        self.view.start_mainloop()

    def bind_widgets(self, start_command, reset_command):
        self.view.start_btn.config(command=start_command)
        self.view.reset_btn.config(command=reset_command)

    def get_user_inputs(self):
        if is_empty(self.view.scan_value.get()):
            raise ValueError("Scan ID is empty")
        if is_empty(self.view.animal_value.get()):
            raise ValueError("Animal ID is empty")
        if is_empty(self.view.experimenter_value.get()):
            raise ValueError("Experimenter ID is empty")

        return (self.view.scan_value.get(),
                self.view.animal_value.get(),
                self.view.experimenter_value.get())

    def enable_user_inputs(self):
        self.view.scan_entry.config(state="normal")
        self.view.animal_entry.config(state="normal")
        self.view.experimenter_entry.config(state="normal")

    def disable_user_inputs(self):
        self.view.scan_entry.config(state="disabled")
        self.view.animal_entry.config(state="disabled")
        self.view.experimenter_entry.config(state="disabled")

    def reset_user_inputs(self):
        self.view.scan_entry.delete(0, tkinter.END)
        self.view.animal_entry.delete(0, tkinter.END)
        self.view.experimenter_entry.delete(0, tkinter.END)

    def display_error(self, error_msg):
        self.view.error_value.set(error_msg)

    def clear_error(self):
        self.view.error_value.set("")

    def reset(self):
        self.reset_user_inputs()
        self.view.sheet.reset()
        self.view.error_value.set("")

# TODO - in another class ?
def is_empty(string) -> bool:
    return True if len(string) == 0 else False
