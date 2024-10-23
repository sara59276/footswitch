import csv
import os
import platform
from datetime import datetime
from os.path import normpath
from stat import S_IREAD

from models.Metadata import Metadata


class FileUtil:

    COLUMNS_COUNT = 3
    EMPTY_LINE = ','.join([''] * COLUMNS_COUNT) + '\n'

    @staticmethod
    def get_destination_folder() -> str:
        root_directory = os.path.abspath(os.sep)
        app_data_directory = os.path.join(root_directory, 'Footswitch', 'data')
        current_year = str(datetime.now().year)
        current_month = str(datetime.now().month).zfill(2)
        current_day = str(datetime.now().day).zfill(2)
        return os.path.join(app_data_directory, current_year, current_month, current_day)

    @staticmethod
    def create_filepath(destination_folder: str, scan_id: str, animal_id: str, experimenter_initials: str, current_date: str) -> str:
        file_name = f"{scan_id}_{animal_id}_{experimenter_initials}_{current_date}.csv"
        return os.path.join(destination_folder, file_name)

    @staticmethod
    def create_new_file(filepath: str, header) -> None:
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory {directory} created")

        if not os.path.exists(filepath):
            with open(filepath, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
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
    def update_metadata(filepath: str, content: list) -> None:
        FileUtil._write_to_csv(filepath, content)

    @staticmethod
    def update_data(filepath: str, content: list) -> None:
        write_position = Metadata.TOTAL_FIELDS + 1
        FileUtil._write_to_csv(filepath, content, write_position)

    @staticmethod
    def clear_metadata(filepath) -> None:
        with open(filepath, "w") as file:
            lines = []
            lines.extend([FileUtil.EMPTY_LINE] * Metadata.TOTAL_FIELDS)
            file.writelines(lines)

    @staticmethod
    def clear_data(filepath) -> None:
        with open(filepath, 'r+') as file:
            file.seek(Metadata.TOTAL_FIELDS + 1)
            file.truncate()

    @staticmethod
    def set_readonly(filepath) -> None:
        if platform.system() == 'Windows':
            os.chmod(filepath, S_IREAD)
        else:  # macOS and Linux
            os.chmod(filepath, 0o444)

    @staticmethod
    def _write_to_csv(filepath: str, content: list, write_position: int = 0) -> None:
        with open(normpath(filepath), mode="w", newline="", encoding="utf-8") as file:
            file.seek(write_position)
            writer = csv.writer(
                file,
                dialect=csv.excel,
                lineterminator="\n",
            )
            writer.writerows(content)
