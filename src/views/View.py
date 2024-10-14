from tkinter import ttk, StringVar, Entry

import tksheet

class View(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.grid(sticky="nsew")
        self._initialize_value_vars()
        self._initialize_frames()
        self._initialize_widgets()
        self._display_frames()
        self._display_widgets()

    def start_mainloop(self):
        self.master.mainloop()

    def _initialize_value_vars(self):
        self.scan_value = StringVar()
        self.animal_value = StringVar()
        self.experimenter_value = StringVar()

    def _initialize_frames(self):
        self.entries_frame = ttk.Frame(self)
        self.sheet_frame = ttk.Frame(self)
        self.control_frame = ttk.Frame(self)

    def _initialize_widgets(self):
        self._initialize_scan()
        self._initialize_animal()
        self._initialize_experimenter()
        self._initialize_sheet()
        self._initialize_control_buttons()

    def _initialize_scan(self):
        self.scan_label = ttk.Label(
            self.entries_frame,
            text="Scan:",
        )
        self.scan_entry = Entry(
            self.entries_frame,
            textvariable=self.scan_value,
            width=15,
            validate="key",
        )

    def _initialize_animal(self):
        self.animal_label = ttk.Label(
            self.entries_frame,
            text="Animal:",
        )
        self.animal_entry = Entry(
            self.entries_frame,
            textvariable=self.animal_value,
            width=15,
            validate="key",
        )

    def _initialize_experimenter(self):
        self.experimenter_label = ttk.Label(
            self.entries_frame,
            text="Experimenter:",
        )
        self.experimenter_entry = Entry(
            self.entries_frame,
            textvariable=self.experimenter_value,
            width=15,
            validate="key",
        )

    def _initialize_sheet(self):
        self.sheet = tksheet.Sheet(self.sheet_frame)
        self.sheet.set_sheet_data([["" for _ in range(3)] for _ in range(1)])
        self.sheet.headers(["event", "start_time", "end_time"])
        self.sheet.readonly_columns([1, 2])
        self.sheet.enable_bindings("single_select",
                               "row_select",
                               "column_width_resize",
                               "arrowkeys",
                               "right_click_popup_menu",
                               "rc_select",
                               "rc_insert_row",
                               "rc_delete_row",
                               "copy",
                               "cut",
                               "paste",
                               "delete",
                               "undo",
                               "edit_cell")

    def _initialize_control_buttons(self):
        self.start_btn = ttk.Button(
            self.control_frame,
            text="START",
        )
        self.reset_btn = ttk.Button(
            self.control_frame,
            text="RESET",
        )

    def _display_frames(self):
        self.entries_frame.grid(row=0, column=0, sticky="nsew")
        self.sheet_frame.grid(row=1, column=0, sticky="nsew")
        self.control_frame.grid(row=1, column=1, sticky="nsew")

    def _display_widgets(self):
        self.scan_label.grid(row=0, column=0, sticky="nsew")
        self.scan_entry.grid(row=0, column=1, sticky="nsew")
        self.animal_label.grid(row=0, column=2, sticky="nsew")
        self.animal_entry.grid(row=0, column=3, sticky="nsew")
        self.experimenter_label.grid(row=0, column=4, sticky="nsew")
        self.experimenter_entry.grid(row=0, column=5, sticky="nsew")
        self.sheet.grid(row=0, column=0, sticky="nsew")
        self.start_btn.grid(row=0, column=0, sticky="nsew")
        self.reset_btn.grid(row=1, column=0, sticky="nsew")