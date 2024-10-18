import csv
import os
import platform
from datetime import datetime
from stat import S_IREAD


class FileManager:

    @staticmethod
    def create_new_empty_file(filepath: str) -> None:
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory {directory} created")

        if not os.path.exists(filepath):
            with open(filepath, 'w') as file:
                file.write('')
            print(f"Created new file : {filepath}")
        else:
            raise FileExistsError(f"The file already exists: {filepath}")

    @staticmethod
    def append(filepath: str, content) -> None:
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(content)

    @staticmethod
    def get_content(filepath) ->  list[list[str]]:
        with open(filepath, mode='r', newline='') as file:
            reader = csv.reader(file)
            content = [row for row in reader]
        return content

    @staticmethod
    def create_filepath(destination_folder: str, scan_id: str, animal_id: str, experimenter_initials: str) -> str:
        current_date = datetime.now().strftime("%Y%m%d")
        file_name = f"{scan_id}_{animal_id}_{experimenter_initials}_{current_date}.csv"
        return os.path.join(destination_folder, file_name)

    @staticmethod
    def get_destination_folder() -> str:
        root_directory = os.path.abspath(os.sep)
        app_data_directory = os.path.join(root_directory, 'footswitch', 'data')
        current_year = str(datetime.now().year)
        current_month = str(datetime.now().month).zfill(2)
        current_day = str(datetime.now().day).zfill(2)
        return os.path.join(app_data_directory, current_year, current_month, current_day)

    @staticmethod
    def clear(filepath) -> None:
        with open(filepath, 'w'):
            pass

    @staticmethod
    def set_readonly(filepath) -> None:
        if platform.system() == 'Windows':
            os.chmod(filepath, S_IREAD)
        else:  # macOS and Linux
            os.chmod(filepath, 0o444)
