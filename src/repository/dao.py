import csv
from abc import ABC, abstractmethod
from os.path import normpath

from models.metadata import Metadata


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

    COLUMNS_COUNT = 3
    EMPTY_LINE = ','.join([''] * COLUMNS_COUNT) + '\n'

    def __init__(self):
        self.__filepath = None # TODO where to store current filepath

    def get_data(self):
        with open(self.__filepath, mode="r", newline="") as file:
            read_position = Metadata.TOTAL_FIELDS + 1
            file.seek(read_position)
            reader = csv.reader(file)
            content = [row for row in reader]
        return content

    def set_metadata(self, metadata):
        self._set(metadata)

    def set_data(self, data):
        write_position = Metadata.TOTAL_FIELDS + 1
        self._set(data, write_position)

    def clear_metadata(self):
        with open(self.__filepath, mode="w") as file:
            lines = []
            lines.extend([self.__class__.EMPTY_LINE] * Metadata.TOTAL_FIELDS)
            file.writelines(lines)

    def clear_data(self):
        with open(self.__filepath, mode="r+") as file:
            file.seek(Metadata.TOTAL_FIELDS + 1)
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