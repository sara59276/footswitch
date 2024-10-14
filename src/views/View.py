from tkinter import ttk, StringVar, Entry


class Vie(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

    def _initialize_value_vars(self):
        self.scan_value = StringVar()
        self.animal_value = StringVar()
        self.experimenter_value = StringVar()

    def _initialize_frames(self):
        self.entries_frame = ttk.Frame(self)
        self.file_frame = ttk.Frame(self)
        self.control_frame = ttk.Frame(self)

    def _initialize_widgets(self):
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

    def _display_frames(self):
        self.entries_frame.grid(row=0, column=0, sticky="we")
        self.file_frame.grid(row=1, column=0, sticky="we")
        self.control_frame.grid(row=1, column=1, sticky="e")

    def _display_widgets(self):
        self.scan_label.grid(row=0, column=0, sticky="w")
        self.scan_entry.grid(row=0, column=1, sticky="w")
        self.animal_label.grid(row=0, column=2, sticky="w")
        self.animal_entry.grid(row=0, column=3, sticky="w")
        self.experimenter_label.grid(row=0, column=4, sticky="w")
        self.experimenter_entry.grid(row=0, column=5, sticky="w")