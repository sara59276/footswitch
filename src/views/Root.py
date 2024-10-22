from tkinter import *

from constants.ui_config import WINDOW_START_WIDTH, WINDOW_START_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT, APP_TITLE
from models.static.ImageManager import ImageManager


class Root(Tk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{WINDOW_START_WIDTH}x{WINDOW_START_HEIGHT}")
        self.minsize(width=WINDOW_MIN_WIDTH, height=WINDOW_MIN_HEIGHT)
        self.title(APP_TITLE)
        window_icon = PhotoImage(file=ImageManager.get_filepath("app_icon.png"))
        self.iconphoto(False, window_icon)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

