import csv
from abc import ABC, abstractmethod
from os.path import normpath


class Dao(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_metadata(self, metadata):
        pass

    @abstractmethod
    def set_data(self, data):
        pass

    @abstractmethod
    def clear_metadata(self):
        pass

    @abstractmethod
    def clear_data(self):
        pass

class FileDao(Dao):

    METADATA_ROWS_COUNT = 7
    COLUMNS_COUNT = 3
    EMPTY_LINE = ','.join([''] * COLUMNS_COUNT) + '\n'

    def __init__(self):
        self.__filepath = None # TODO where to store current filepath

    def get_data(self):
        with open(self.__filepath, mode="r", newline="") as file:
            read_position = self.__class__.METADATA_ROWS_COUNT
            file.seek(read_position)
            reader = csv.reader(file)
            content = [row for row in reader]
        return content

    def set_metadata(self, metadata):
        self._set(metadata)

    def set_data(self, data):
        write_position = self.__class__.METADATA_ROWS_COUNT
        self._set(data, write_position)

    def clear_metadata(self):
        with open(self.__filepath, mode="w") as file:
            lines = []
            lines.extend([self.__class__.EMPTY_LINE] * self.__class__.METADATA_ROWS_COUNT)
            file.writelines(lines)

    def clear_data(self):
        with open(self.__filepath, mode="r+") as file:
            file.seek(self.__class__.METADATA_ROWS_COUNT)
            file.truncate()

    def _set(self, content, write_position: int = 0):
        with open(normpath(self.__filepath), mode="w", newline="", encoding="utf-8") as file:
            file.seek(write_position)
            writer = csv.writer(
                file,
                dialect=csv.excel,
                lineterminator="\n",
            )
            writer.writerows(content)