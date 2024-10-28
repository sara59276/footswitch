import tkinter
from tkinter import ttk
from tkinter.constants import NORMAL, DISABLED

from Demos.win32ts_logoff_disconnected import session

from views.view import View


class ViewManager:
    def __init__(self, view: View):
        self.__view = view
        self._initialize_styles()

    def start_mainloop(self) -> None:
        self.__view.start_mainloop()

    def bind_buttons(self, start_command, end_command, clear_command) -> None:
        self.__view.start_btn.config(command=start_command)
        self.__view.end_btn.config(command=end_command)
        self.__view.clear_btn.config(command=clear_command)

    def bind_footswitch(self, footswitch_key, footswitch_pressed, footswitch_released) -> None:
        self.__view.master.bind(f"<{footswitch_key}>", footswitch_pressed)
        self.__view.master.bind(f"<KeyRelease-{footswitch_key}>", footswitch_released)

    def bind_entry_constraints(self, validate_scan_and_animal_inputs, validate_experimenter_input) -> None:
        validate_file_compatible = (self.__view.register(validate_scan_and_animal_inputs), "%S")
        self.__view.scan_entry.config(validatecommand=validate_file_compatible)
        self.__view.animal_entry.config(validatecommand=validate_file_compatible)

        validate_initials = (self.__view.register(validate_experimenter_input), "%S")
        self.__view.experimenter_entry.config(validatecommand=validate_initials)

    def bind_sheet(self, on_sheet_modified) -> None:
        self.__view.sheet.bind("<<SheetModified>>", on_sheet_modified)

    def bind_close_window_button(self, on_close_window_button) -> None:
        self.__view.get_root().protocol("WM_DELETE_WINDOW", on_close_window_button)

    def activate_start_button(self) -> None:
        self.__view.start_btn.config(state=NORMAL)

    def deactivate_start_button(self) -> None:
        self.__view.start_btn.config(state=DISABLED)

    def activate_end_button(self) -> None:
        self.__view.end_btn.config(state=NORMAL)

    def deactivate_end_button(self) -> None:
        self.__view.end_btn.config(state=DISABLED)

    def get_user_inputs(self) -> tuple[str, str, str]:
        if is_empty(self.__view.scan_value.get()):
            raise ValueError("Scan ID is empty")
        if is_empty(self.__view.animal_value.get()):
            raise ValueError("Animal ID is empty")
        if is_empty(self.__view.experimenter_value.get()):
            raise ValueError("Experimenter ID is empty")
        if is_invalid_initials(self.__view.experimenter_value.get()):
            raise ValueError("Experimenter initials should be of length 2 to 3")

        return (self.__view.scan_value.get(),
                self.__view.animal_value.get(),
                self.__view.experimenter_value.get())

    def enable_user_inputs(self) -> None:
        self.__view.scan_entry.config(state="normal")
        self.__view.animal_entry.config(state="normal")
        self.__view.experimenter_entry.config(state="normal")

    def disable_user_inputs(self) -> None:
        self.__view.scan_entry.config(state="disabled")
        self.__view.animal_entry.config(state="disabled")
        self.__view.experimenter_entry.config(state="disabled")

    def reset_user_inputs(self) -> None:
        self.enable_user_inputs()
        self.__view.scan_entry.delete(0, tkinter.END)
        self.__view.animal_entry.delete(0, tkinter.END)
        self.__view.experimenter_entry.delete(0, tkinter.END)

    def display_session_start(self, session_start):
        self.__view.session_start_value.set(session_start)

    def display_session_end(self, session_end):
        self.__view.session_end_value.set(session_end)

    def add_start_time(self, start_time):
        start_time_col = "B"
        last_row_index = self.__view.sheet.get_total_rows()
        start_time_cell = f"{start_time_col}{last_row_index}"
        self.__view.sheet.span(start_time_cell).data = [start_time]

    def add_end_time(self, end_time):
        end_time_col = "C"
        last_row_index = self.__view.sheet.get_total_rows()
        start_time_cell = f"{end_time_col}{last_row_index}"
        self.__view.sheet.span(start_time_cell).data = [end_time]

    def set_sheet(self, data) -> None:
        self.__view.sheet.readonly(
            self.__view.sheet.span("B:C"),
            readonly=True,
        )
        self.__view.sheet.readonly(
            self.__view.sheet.span("A1"),
            readonly=True,
        )
        self.set_sheet_content(data)

    def set_sheet_content(self, data) -> None:
        self.__view.sheet.set_sheet_data(data)
        self.append_empty_row_to_sheet()

    def get_sheet_content(self) -> object:
        return self.__view.sheet.data

    def append_empty_row_to_sheet(self) -> None:
        if self._is_sheet_populated():
            self.__view.sheet.insert_row()

    def pop_empty_row_in_sheet(self) -> None:
        if self._is_sheet_populated():
            last_row_idx = self.__view.sheet.get_total_rows() - 1
            self.__view.sheet.del_row(idx=last_row_idx)

    def _is_sheet_populated(self) -> bool:
        return self.__view.sheet.get_total_rows() > 0 and self.__view.sheet.get_total_columns() > 0

    def sheet_scroll_down(self) -> None:
        last_row_index = self.__view.sheet.get_total_rows() - 1
        self.__view.sheet.see(last_row_index)

    def display_footswitch_released_icon(self) -> None:
        self.__view.fs_pressed_icon_label.grid_forget()
        self.__view.fs_released_icon_label.grid(row=0, column=0, sticky="ew", padx=5)

    def display_footswitch_pressed_icon(self) -> None:
        self.__view.fs_released_icon_label.grid_forget()
        self.__view.fs_pressed_icon_label.grid(row=0, column=0, sticky="ew", padx=5)

    def display_footswitch_disconnected(self) -> None:
        self.__view.device_value.set("FootSwitch FS22 is disconnected")
        self.__view.device_connection_label.config(style="Red.TLabel")

    def display_footswitch_connected(self) -> None:
        self.__view.device_value.set("FootSwitch FS22 is connected")
        self.__view.device_connection_label.config(style="Green.TLabel")

    def display_error(self, content: str) -> None:
        self.__view.msg_value.set(content)
        self.__view.msg_label.config(style="Red.TLabel")

    def display_success(self, content: str) -> None:
        self.__view.msg_value.set(content)
        self.__view.msg_label.config(style="Green.TLabel")

    def clear_msg(self) -> None:
        self.__view.msg_value.set("")

    def reset_view(self) -> None:
        self.reset_user_inputs()
        self.__view.msg_value.set("")
        self.__view.session_start_value.set("")
        self.__view.session_end_value.set("")
        self.__view.sheet.reset()

    def get_root(self):
        return self.__view.get_root()

    def _initialize_styles(self) -> None:
        style = ttk.Style()
        style.configure("Red.TLabel", foreground="red")
        style.configure("Green.TLabel", foreground="green")

# TODO - in another class ?
def is_empty(string: str) -> bool:
    return True if len(string) == 0 else False

def is_invalid_initials(string: str) -> bool:
    return not (2 <= len(string) <= 3)
