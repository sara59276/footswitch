import csv
import os
from datetime import datetime


class Sheet:
    def __init__(self):
        self.__filepath = None

    def create_new_file(self, destination_folder: str, scan_id: str, animal_id: str) -> str:
        filepath = self._get_filepath(destination_folder, scan_id, animal_id)

        if os.path.exists(filepath):
            raise FileExistsError(f"The file already exists: {filepath}")

        self.__filepath = filepath

        column_names = ["event", "start_time", "end_time"]
        with open(self.__filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(column_names)

        print(f"Created new file : {self.__filepath}")
        return self.__filepath

    def get_file_content(self) ->  list[list[str]]:
        with open(self.__filepath, mode='r', newline='') as file:
            reader = csv.reader(file)
            content = [row for row in reader]
        return content

    def append_measure(self, measure_data) -> None: # TODO add measure_data variable type
        with open(self.__filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(measure_data)

    def reset(self) -> None:
        self.__filepath = None

    def _get_filepath(self, destination_folder: str, scan_id: str, animal_id: str) -> str:
        current_date = datetime.now().strftime("%Y%m%d")
        file_name = f"{scan_id}_{animal_id}_{current_date}.csv"
        return os.path.join(destination_folder, file_name)