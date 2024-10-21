from tkinter import Tk

from constants.ui_config import WINDOW_START_WIDTH, WINDOW_START_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT, APP_TITLE
from models.ImageManager import ImageManager


class Root(Tk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{WINDOW_START_WIDTH}x{WINDOW_START_HEIGHT}")
        self.minsize(width=WINDOW_MIN_WIDTH, height=WINDOW_MIN_HEIGHT)
        self.title(APP_TITLE)
        self.iconbitmap(ImageManager.get_app_icon())
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

