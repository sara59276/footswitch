from tkinter import *
from constants.ui import WINDOW_START_WIDTH, WINDOW_START_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT, APP_TITLE
from utils.image_utils import ImageUtil


class Root(Tk):
    def __init__(self):
        super().__init__()
        self._set_window_sizes()
        self._set_window_title()
        self._set_window_icon()
        self._configure_grid()

    def _set_window_sizes(self) -> None:
        self.geometry(f"{WINDOW_START_WIDTH}x{WINDOW_START_HEIGHT}")
        self.minsize(width=WINDOW_MIN_WIDTH, height=WINDOW_MIN_HEIGHT)

    def _set_window_title(self) -> None:
        self.title(APP_TITLE)

    def _set_window_icon(self) -> None:
        window_icon = PhotoImage(file=ImageUtil.get_filepath("app_icon.png"))
        self.iconphoto(False, window_icon)

    def _configure_grid(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

