from tkinter import ttk, StringVar, Entry

import tksheet

from utils.ImageUtil import ImageUtil


class View(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.__container = container
        self.grid()
        self._initialize_value_vars()
        self._initialize_frames()
        self._initialize_widgets()
        self._display_frames()
        self._display_widgets()

    def start_mainloop(self) -> None:
        self.master.mainloop()

    def get_root(self):
        return self.__container

    def set_sheet(self, data) -> None:
        self.sheet.set_sheet_data(data)
        self.append_empty_row()

    def append_empty_row(self) -> None:
        self.sheet.insert_row()

    def sheet_scroll_down(self) -> None:
        last_row_index = self.sheet.get_total_rows() - 1
        self.sheet.see(last_row_index)

    def _initialize_value_vars(self) -> None:
        self.scan_value = StringVar()
        self.animal_value = StringVar()
        self.experimenter_value = StringVar()
        self.device_value = StringVar()
        self.msg_value = StringVar()

    def _initialize_frames(self) -> None:
        self.entries_frame = ttk.Frame(self)
        self.sheet_frame = ttk.Frame(self)
        self.control_frame = ttk.Frame(self)
        self.device_connection_frame = ttk.Frame(self)
        self.msg_frame = ttk.Frame(self)

    def _initialize_widgets(self) -> None:
        self._initialize_scan()
        self._initialize_animal()
        self._initialize_experimenter()
        self._initialize_sheet()
        self._initialize_control_buttons()
        self._initialize_footswitch_icon_labels()
        self._initialize_device_connection_label()
        self._initialize_msg_label()

    def _initialize_scan(self) -> None:
        self.scan_label = ttk.Label(
            self.entries_frame,
            text="Scan ID:",
        )
        self.scan_entry = Entry(
            self.entries_frame,
            textvariable=self.scan_value,
            width=15,
            validate="key",
        )

    def _initialize_animal(self) -> None:
        self.animal_label = ttk.Label(
            self.entries_frame,
            text="Animal ID:",
        )
        self.animal_entry = Entry(
            self.entries_frame,
            textvariable=self.animal_value,
            width=15,
            validate="key",
        )

    def _initialize_experimenter(self) -> None:
        self.experimenter_label = ttk.Label(
            self.entries_frame,
            text="Experimenter initials:",
        )
        self.experimenter_entry = Entry(
            self.entries_frame,
            textvariable=self.experimenter_value,
            width=15,
            validate="key",
        )

    def _initialize_sheet(self) -> None:
        self.sheet = tksheet.Sheet(
            self.sheet_frame,
            width=550,
            height=450,
            default_column_width=170,
        )
        self.sheet.enable_bindings("single_select",
                               "row_select",
                               "arrowkeys",
                               "rc_select",
                               "copy",
                               "paste",
                               "undo",
                               "edit_cell"
        )

    def _initialize_control_buttons(self) -> None:
        self.start_btn = ttk.Button(
            self.control_frame,
            text="START",
        )
        self.end_btn = ttk.Button(
            self.control_frame,
            text="END",
        )
        self.clear_btn = ttk.Button(
            self.control_frame,
            text="CLEAR",
        )
        for button in (self.start_btn, self.end_btn, self.clear_btn):
            button.config(width=15, padding=30)

    def _initialize_footswitch_icon_labels(self) -> None:
        self.fs_released_icon = ImageUtil.get_image("footswitch_released_icon.png")
        self.fs_released_icon_label = ttk.Label(
            self.device_connection_frame,
            image=self.fs_released_icon
        )
        self.fs_pressed_icon = ImageUtil.get_image("footswitch_pressed_icon.png")
        self.fs_pressed_icon_label = ttk.Label(
            self.device_connection_frame,
            image=self.fs_pressed_icon
        )

    def _initialize_device_connection_label(self) -> None:
        self.device_connection_label = ttk.Label(
            self.device_connection_frame,
            textvariable=self.device_value,
        )

    def _initialize_msg_label(self) -> None:
        self.msg_label = ttk.Label(
            self.msg_frame,
            textvariable=self.msg_value,
        )

    def _display_frames(self) -> None:
        self.entries_frame.grid(row=0, column=0, padx=20, pady=20)
        self.device_connection_frame.grid(row=0, column=1, padx=10, pady=20)
        self.msg_frame.grid(row=1, column=0, sticky="nsew", padx=20)
        self.sheet_frame.grid(row=2, column=0, padx=20, pady=20)
        self.control_frame.grid(row=2, column=1, sticky="ew", padx=20, pady=20)

    def _display_widgets(self) -> None:
        self.scan_label.grid(row=0, column=0, sticky="e", padx=5)
        self.scan_entry.grid(row=0, column=1, sticky="w", padx=5)
        self.animal_label.grid(row=0, column=2, sticky="e", padx=5)
        self.animal_entry.grid(row=0, column=3, sticky="w", padx=5)
        self.experimenter_label.grid(row=0, column=4, sticky="e", padx=5)
        self.experimenter_entry.grid(row=0, column=5, sticky="w", padx=5)
        self.sheet.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.start_btn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.end_btn.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.clear_btn.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.device_connection_label.grid(row=0, column=1, sticky="ew", padx=5)
        self.msg_label.grid(row=0, column=0, sticky="ew", padx=5)

