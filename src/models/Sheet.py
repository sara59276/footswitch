import csv
import os
from datetime import datetime


class Sheet:
    def __init__(self):
        self.__filepath = None

    def create_new_file(self, destination_folder, scan_id, animal_id):
        if self.__filepath is not None:
            raise FileExistsError(f"This file already exists : {self.__filepath}")

        current_date = datetime.now().strftime("%Y%m%d")
        file_name = f"{scan_id}_{animal_id}_{current_date}.csv"
        self.__filepath = os.path.join(destination_folder, file_name)

        column_names = ["event", "start_time", "end_time"]
        with open(self.__filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(column_names)

        print(f"Created new file : {self.__filepath}")