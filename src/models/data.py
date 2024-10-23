from repo.repository import FileRepository


class Data:

    HEADER = ['event', 'start_time', 'end_time']

    def __init__(self):
        self.__repo = FileRepository()

    def get(self, filepath: str):
        return self.__repo.get_data(filepath)

    def update(self, filepath: str, data = None) -> None:
        if data is None:
            self.__repo.set_data(filepath, self.__class__.HEADER)
        else:
            cleaned_data = self._pop_empty_last_row(data)
            self.__repo.clear_data(filepath)
            self.__repo.set_data(filepath, cleaned_data)

    def _pop_empty_last_row(self, data):
        if data and not any(cell.strip() for cell in data[-1]):
            data.pop()
        return data