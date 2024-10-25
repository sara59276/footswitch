import csv
import os
import platform
from datetime import datetime
from stat import S_IREAD


class FileUtil:

    @staticmethod
    def get_destination_folder() -> str:
        root_directory = os.path.abspath(os.sep)
        app_data_directory = os.path.join(root_directory, 'Footswitch', 'data')
        current_year = str(datetime.now().year)
        current_month = str(datetime.now().month).zfill(2)
        current_day = str(datetime.now().day).zfill(2)
        return os.path.join(app_data_directory, current_year, current_month, current_day)

    @staticmethod
    def create_file(scan_id: str, animal_id: str, experimenter_initials: str, current_date: str) -> str:
        filename = f"{scan_id}_{animal_id}_{experimenter_initials}_{current_date}.csv"

        dest_folder = FileUtil.get_destination_folder()
        filepath = os.path.join(dest_folder, filename)
        FileUtil.create_new_file(filepath)
        return filepath

    @staticmethod
    def create_new_file(filepath: str) -> None:
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory {directory} created")

        if not os.path.exists(filepath):
            with open(filepath, mode="w", newline="") as file:
                pass
            print(f"Created new file : {filepath}")
        else:
            raise FileExistsError(f"This file already exists: {filepath}")

    @staticmethod
    def get_content(filepath) ->  list[list[str]]:
        with open(filepath, mode='r', newline='') as file:
            reader = csv.reader(file)
            content = [row for row in reader]
        return content


    @staticmethod
    def set_readonly(filepath) -> None:
        if platform.system() == 'Windows':
            os.chmod(filepath, S_IREAD)
        else:  # macOS and Linux
            os.chmod(filepath, 0o444)
