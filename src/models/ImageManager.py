from pathlib import Path

from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage


class ImageManager:

    @staticmethod
    def get_image(name: str,  width: int = 30, height: int = 30) -> PhotoImage:
        base_dir = Path(__file__).resolve().parent
        src_dir = base_dir.parent
        icon_file = f"{name}_icon.png"
        icon_path = src_dir / 'resources' / 'images' / icon_file
        icon = Image.open(icon_path)
        resized_icon = icon.resize((width, height))
        return ImageTk.PhotoImage(resized_icon)

    @staticmethod
    def get_app_icon():
        base_dir = Path(__file__).resolve().parent
        src_dir = base_dir.parent
        return src_dir / 'resources' / 'images' / 'app_icon.ico'
