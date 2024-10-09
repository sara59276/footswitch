from typing import TypedDict

from views.Root import Root

from views.MainView import MainView


class Frames(TypedDict):
    main_view: MainView

class View:
    def __init__(self):
        self.root = Root()
        self.menubar = None
        self.frames: Frames = {}

        self._add_frame(MainView, "main_view")

    def _add_frame(self, frame, name: str):
        self.frames[name] = frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()