from models.FileManager import FileManager


class DataSheet:

    HEADER = ['event', 'start_time', 'end_time']

    def __init__(self):
        self.__filepath= None

    def initialize(self, filepath: str) -> None:
        self.__filepath = filepath
        FileManager.create_new_file(filepath, DataSheet.HEADER)

    def get_data_from_file(self):
        return FileManager.get_content(self.__filepath)

    def update(self, data) -> None:
        if self.__filepath is not None:
            FileManager.clear(self.__filepath)
            FileManager.append(self.__filepath, data)

    def reset(self):
        self.__filepath = None

    def set_readonly(self):
        if self.__filepath is not None:
            FileManager.set_readonly(self.__filepath)

