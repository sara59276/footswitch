from pathlib import Path
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage

from utils.file_utils import FileUtil


class ImageUtil:

    @staticmethod
    def get_path(image_name: str) -> Path:
        path = FileUtil.get_project_root() / 'resources' / 'img' / image_name

        if not path.exists():
            raise FileNotFoundError(f"The file '{path}' does not exist.")

        return path

    @staticmethod
    def get_image(filename: str, width: int = 30, height: int = 30) -> PhotoImage:
        icon_path = ImageUtil.get_path(filename)
        icon = Image.open(icon_path)
        resized_icon = icon.resize((width, height))
        return ImageTk.PhotoImage(resized_icon)
