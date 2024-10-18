from models import MeasureRow
from models.FileManager import FileManager


class DataSheet:

    HEADER = ["event", "start_time", "end_time"]

    def __init__(self):
        self.__filepath= None

    def initialize(self, filepath: str) -> None:
        self.__filepath = filepath
        FileManager.create_new_empty_file(filepath)
        FileManager.append_row(filepath, DataSheet.HEADER)

    def get_data(self):
        return FileManager.get_content(self.__filepath)

    def append_measure_row(self, measure_row: MeasureRow) -> None:
        FileManager.append_row(self.__filepath, measure_row.get_row())

    def reset(self):
        self.__filepath = None


