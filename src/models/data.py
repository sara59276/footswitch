from repositories.repository import FileRepository


class Data:

    HEADER = [['event', 'start_time', 'end_time']]

    def __init__(self):
        self.__repo = FileRepository()

    def get(self, filepath: str) -> list[list[str]]:
        return self.__repo.get_data(filepath)

    def update(self, filepath: str, data = None) -> None:
        if data is None:
            self.__repo.overwrite_data(filepath, self.__class__.HEADER)
        else:
            self.__repo.clear_data(filepath)
            self.__repo.overwrite_data(filepath, data)
