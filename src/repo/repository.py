from abc import ABC, abstractmethod

from repo.dao import FileDao
from repo.exception import RepositoryException


class Repository(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_metadata(self, metadata):
        pass

    @abstractmethod
    def clear_metadata(self):
        pass

    @abstractmethod
    def clear_data(self):
        pass

    @abstractmethod
    def set_data(self, data):
        pass

class FileRepository(Repository):
    def __init__(self):
        self.__dao = FileDao()

    def get_data(self):
        self.__dao.get_data()

    def set_metadata(self, metadata):
        if metadata is None or len(metadata) == 0:
            raise RepositoryException("Metadata can't be empty")
        self.__dao.set_metadata(metadata)

    def clear_metadata(self):
        self.__dao.clear_metadata()

    def clear_data(self):
        self.__dao.clear_data()

    def set_data(self, data):
        if data is None or len(data) == 0:
            raise RepositoryException("Data can't be empty")
        self.__dao.set_data(data)

