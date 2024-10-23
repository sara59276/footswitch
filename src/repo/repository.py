from abc import ABC, abstractmethod

from repo.dao import FileDao
from repo.exception import RepositoryException


class Repository(ABC):
    @abstractmethod
    def get_data(self, filepath):
        pass

    @abstractmethod
    def set_metadata(self, filepath, metadata):
        pass

    @abstractmethod
    def clear_metadata(self, filepath):
        pass

    @abstractmethod
    def clear_data(self, filepath):
        pass

    @abstractmethod
    def set_data(self, filepath, data):
        pass

class FileRepository(Repository):
    def __init__(self):
        self.__dao = FileDao()

    def get_data(self, filepath):
        self.__dao.get_data(filepath)

    def set_metadata(self, filepath, metadata):
        if metadata is None or len(metadata) == 0:
            raise RepositoryException("Metadata can't be empty")
        self.__dao.set_metadata(filepath, metadata)

    def clear_metadata(self, filepath):
        self.__dao.clear_metadata(filepath)

    def clear_data(self, filepath):
        self.__dao.clear_data(filepath)

    def set_data(self, filepath, data):
        if data is None or len(data) == 0:
            raise RepositoryException("Data can't be empty")
        self.__dao.set_data(filepath, data)

