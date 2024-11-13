from abc import ABC, abstractmethod

from utils.file_utils import FileUtil


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

    METADATA_ROWS_COUNT = 8 # TODO - magic number, but circular import problem
    EMPTY_LINE: list[str] = []

    def overwrite_metadata(self, filepath, content: list[list[str]]):
        content.append(FileDao.EMPTY_LINE)
        FileUtil.write(filepath, content)

    def get_data(self, filepath) -> list[list[str]]:
        return FileUtil.read(filepath, skip_rows=self.__class__.METADATA_ROWS_COUNT)

    def overwrite_data(self, filepath, content):
        FileUtil.write(filepath, content, skip_rows=self.__class__.METADATA_ROWS_COUNT)

    def clear_data(self, filepath):
        skip_rows = self.__class__.METADATA_ROWS_COUNT
        with open(filepath, mode="r+") as file:
            for _ in range(skip_rows):
                file.readline()
            file.seek(file.tell())
            file.truncate()
