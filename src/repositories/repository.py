from abc import ABC, abstractmethod

from repositories.dao import FileDao
from repositories.exception import RepositoryException


class Repository(ABC):
    @abstractmethod
    def overwrite_metadata(self, filepath, metadata):
        pass

    @abstractmethod
    def get_data(self, filepath):
        pass

    @abstractmethod
    def clear_data(self, filepath):
        pass

    @abstractmethod
    def set_data(self, filepath, data):
        pass

class FileRepository(Repository):
    def overwrite_metadata(self, filepath, metadata):
        if metadata is None or len(metadata) == 0:
            raise RepositoryException("Metadata can't be empty")
        self.__dao.overwrite_metadata(filepath, metadata)

    def __init__(self):
        self.__dao = FileDao()

    def get_data(self, filepath) -> list[list[str]]:
        return self.__dao.get_data(filepath)

    def set_data(self, filepath, data):
        if data is None or len(data) == 0:
            raise RepositoryException("Data can't be empty")
        self.__dao.set_data(filepath, data)

    def clear_data(self, filepath):
        self.__dao.clear_data(filepath)

