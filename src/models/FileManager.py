import csv
import os
from datetime import datetime


class FileManager:

    @staticmethod
    def create_new_empty_file(filepath: str) -> bool:
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
    def append_row(filepath: str, row_content: list[str]) -> None: # TODO add measure_data variable type
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row_content)

    @staticmethod
    def update_row(filepath: str, row_content: str, row_index: int) -> None:
        pass

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
