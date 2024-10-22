from pathlib import Path

from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage


class ImageManager:

    @staticmethod
    def get_filepath(filename: str) -> Path:
        base_dir = Path(__file__).resolve().parent.parent
        src_dir = base_dir.parent
        return src_dir / 'resources' / 'images' / filename

    @staticmethod
    def get_image(filename: str, width: int = 30, height: int = 30) -> PhotoImage:
        icon_path = ImageManager.get_filepath(filename)
        icon = Image.open(icon_path)
        resized_icon = icon.resize((width, height))
        return ImageTk.PhotoImage(resized_icon)
