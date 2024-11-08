from pathlib import Path
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage

from constants.app_directory import APP_DIRECTORY


class ImageUtil:

    @staticmethod
    def get_filepath(filename: str) -> Path:
        return APP_DIRECTORY / 'resources' / 'images' / filename

    @staticmethod
    def get_image(filename: str, width: int = 30, height: int = 30) -> PhotoImage:
        icon_path = ImageUtil.get_filepath(filename)
        icon = Image.open(icon_path)
        resized_icon = icon.resize((width, height))
        return ImageTk.PhotoImage(resized_icon)
