import tkinter
from tkinter import ttk

from views.View import View


class ViewFacade:
    def __init__(self, view: View):
        self.view = view
        self._initialize_styles()

    def start_mainloop(self) -> None:
        self.view.start_mainloop()

    def bind_widgets(self, start_command, reset_command) -> None:
        self.view.start_btn.config(command=start_command)
        self.view.reset_btn.config(command=reset_command)

    def bind_footswitch(self, footswitch_pressed, footswitch_released) -> None:
        self.view.master.bind("&", footswitch_pressed)
        self.view.master.bind("<KeyRelease-&>", footswitch_released)

    def get_user_inputs(self) -> tuple[str, str, str]:
        if is_empty(self.view.scan_value.get()):
            raise ValueError("Scan ID is empty")
        if is_empty(self.view.animal_value.get()):
            raise ValueError("Animal ID is empty")
        if is_empty(self.view.experimenter_value.get()):
            raise ValueError("Experimenter ID is empty")

        return (self.view.scan_value.get(),
                self.view.animal_value.get(),
                self.view.experimenter_value.get())

    def enable_user_inputs(self) -> None:
        self.view.scan_entry.config(state="normal")
        self.view.animal_entry.config(state="normal")
        self.view.experimenter_entry.config(state="normal")

    def disable_user_inputs(self) -> None:
        self.view.scan_entry.config(state="disabled")
        self.view.animal_entry.config(state="disabled")
        self.view.experimenter_entry.config(state="disabled")

    def reset_user_inputs(self) -> None:
        self.enable_user_inputs()
        self.view.scan_entry.delete(0, tkinter.END)
        self.view.animal_entry.delete(0, tkinter.END)
        self.view.experimenter_entry.delete(0, tkinter.END)

    def update_sheet(self, data) -> None:
        self.view.update_sheet(data)

    def get_last_measure(self) -> list[object]:
        last_row_index = self.view.sheet.get_total_rows() - 1
        row_content = self.view.sheet.get_row_data(last_row_index)
        return row_content

    def display_footswitch_disconnected(self) -> None:
        self.view.device_value.set("FootSwitch FS22 is disconnected")
        self.view.device_label.config(style="Red.TLabel")

    def display_footswitch_connected(self) -> None:
        self.view.device_value.set("FootSwitch FS22 is connected")
        self.view.device_label.config(style="Green.TLabel")

    def display_error(self, content: str) -> None:
        self.view.msg_value.set(content)
        self.view.msg_label.config(style="Red.TLabel")

    def display_success(self, content: str) -> None:
        self.view.msg_value.set(content)
        self.view.msg_label.config(style="Green.TLabel")

    def clear_msg(self) -> None:
        self.view.msg_value.set("")

    def reset_view(self) -> None:
        self.reset_user_inputs()
        self.view.sheet.reset()
        self.view.msg_value.set("")

    def _initialize_styles(self) -> None:
        style = ttk.Style()
        style.configure("Red.TLabel", foreground="red")
        style.configure("Green.TLabel", foreground="green")

# TODO - in another class ?
def is_empty(string: str) -> bool:
    return True if len(string) == 0 else False
