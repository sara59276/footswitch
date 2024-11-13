import csv
from abc import ABC, abstractmethod
from os.path import normpath


class Dao(ABC):
    @abstractmethod
    def overwrite_metadata(self, filepath, metadata):
        pass

    @abstractmethod
    def get_data(self, filepath):
        pass

    @abstractmethod
    def overwrite_data(self, filepath, data):
        pass

    @abstractmethod
    def clear_data(self, filepath):
        pass

class FileDao(Dao):

    METADATA_ROWS_COUNT = 7 # TODO - magic number
    EMPTY_LINE: list[str] = []

    def overwrite_metadata(self, filepath, content: list[list[str]]):
        content.append(FileDao.EMPTY_LINE)
        self._write(filepath, content)

    def get_data(self, filepath) -> list[list[str]]:
        return self._read(filepath, skip_rows=self.__class__.METADATA_ROWS_COUNT)

    def overwrite_data(self, filepath, content):
        self._write(filepath, content, skip_rows=self.__class__.METADATA_ROWS_COUNT)

    def clear_data(self, filepath):
        skip_rows = self.__class__.METADATA_ROWS_COUNT
        with open(filepath, mode="r+") as file:
            for _ in range(skip_rows):
                file.readline()
            file.seek(file.tell())
            file.truncate()

    def _read(self, filepath, skip_rows = 0) -> list[list[str]]:
        with open(normpath(filepath), mode="r", newline="") as file:
            for _ in range(skip_rows):
                file.readline()
            reader = csv.reader(file)
            content = [row for row in reader]
        return content

    def _write(self, filepath, content, skip_rows = 0) -> None:
        with open(normpath(filepath), mode="r+") as file:
            for _ in range(skip_rows):
                file.readline()
            writer = csv.writer(file, dialect=csv.excel, lineterminator="\n",)
            writer.writerows(content)
