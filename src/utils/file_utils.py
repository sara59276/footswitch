import csv
import os
import platform
import sys
from os.path import normpath
from pathlib import Path
from stat import S_IREAD

from constants.app_directory import APP_DIRECTORY


class FileUtil:

    @staticmethod
    def create_file(destination_folder: str, scan_id: str, animal_id: str, experimenter_initials: str, current_date: str) -> str:
        filename = f"{scan_id}_{animal_id}_{experimenter_initials}_{current_date}.csv"
        destination_folder = destination_folder
        filepath = os.path.join(destination_folder, filename)

        os.makedirs(destination_folder, exist_ok=True)
        if not os.path.isfile(filepath):
            with open(filepath, mode="w", newline=""):
                pass
            print(f"File created at: {filepath}")
        else:
            filename = FileUtil.get_filename(filepath)
            folder = FileUtil.get_folder(filepath)
            raise FileExistsError(f"This file already exists: {filename}"
                                  f"\nIn folder: {folder}")

        return filepath

    @staticmethod
    def set_readonly(filepath) -> None:
        if platform.system() == 'Windows':
            os.chmod(filepath, S_IREAD)
        else:  # macOS and Linux
            os.chmod(filepath, 0o444)

    @staticmethod
    def read(filepath: str, skip_rows: int = 0) -> list[list[str]]:
        with open(normpath(filepath), mode="r", newline="") as file:
            for _ in range(skip_rows):
                file.readline()
            reader = csv.reader(file)
            content = [row for row in reader]
        return content

    @staticmethod
    def write(filepath: str, content: list[list[str]], skip_rows: int = 0) -> None:
        with open(normpath(filepath), mode="r+") as file:
            for _ in range(skip_rows):
                file.readline()
            writer = csv.writer(file, dialect=csv.excel, lineterminator="\n",)
            writer.writerows(content)

    @staticmethod
    def get_project_root():
        if getattr(sys, 'frozen', False):
            project_root = Path(getattr(sys, '_MEIPASS', ''))
        else:
            project_root = APP_DIRECTORY

        return project_root

    @staticmethod
    def get_folder(filepath: str) -> str:
        return os.path.dirname(filepath)

    @staticmethod
    def get_filename(filepath: str) -> str:
        return os.path.basename(filepath)
