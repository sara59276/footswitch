import csv
from abc import ABC, abstractmethod
from os.path import normpath


class Dao(ABC):
    @abstractmethod
    def get_data(self, filepath):
        pass

    @abstractmethod
    def set_metadata(self, filepath, metadata):
        pass

    @abstractmethod
    def set_data(self, filepath, data):
        pass

    @abstractmethod
    def clear_metadata(self, filepath):
        pass

    @abstractmethod
    def clear_data(self, filepath):
        pass

class FileDao(Dao):

    METADATA_ROWS_COUNT = 7
    COLUMNS_COUNT = 3
    EMPTY_LINE = ','.join([''] * COLUMNS_COUNT) + '\n'

    def get_data(self, filepath):
        with open(filepath, mode="r", newline="") as file:
            read_position = self.__class__.METADATA_ROWS_COUNT
            file.seek(read_position)
            reader = csv.reader(file)
            content = [row for row in reader]
        return content

    def set_metadata(self, filepath, metadata):
        self._set(filepath, metadata)

    def set_data(self, filepath, data):
        write_position = self.__class__.METADATA_ROWS_COUNT
        print("write position:", write_position)
        self._set(filepath, data, write_position)

    def clear_metadata(self, filepath):
        with open(filepath, mode="w") as file:
            lines = []
            lines.extend([self.__class__.EMPTY_LINE] * self.__class__.METADATA_ROWS_COUNT)
            file.writelines(lines)

    def clear_data(self, filepath):
        with open(filepath, mode="r+") as file:
            file.seek(self.__class__.METADATA_ROWS_COUNT)
            file.truncate()

    def _set(self, filepath, content, write_row: int = 0):
        print("in dao set, write row:", write_row)
        print("in dao set, content :\n", content)

        with open(normpath(filepath), mode="r+", newline="", encoding="utf-8") as file:
            for _ in range(self.METADATA_ROWS_COUNT):
                next(file)

            writer = csv.writer(
                file,
                dialect=csv.excel,
                lineterminator="\n",
            )
            writer.writerows(content)

        print("in dao, file content:\n", self.get_data(filepath))