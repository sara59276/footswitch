from utils.FileUtil import FileUtil
from utils.TimeUtil import TimeUtil


class Data:

    HEADER = ['event', 'start_time', 'end_time']

    def __init__(self):
        self.__filepath= None

        self.__events: list[str] = []
        self.__start_times: list[str] = []
        self.__end_times: list[str] = []

    def initialize(self, scan_id, animal_id, experimenter_initials) -> str:
        self.__filepath = FileUtil.create_filepath(
            destination_folder=FileUtil.get_destination_folder(),
            scan_id=scan_id,
            animal_id=animal_id,
            experimenter_initials=experimenter_initials.upper(),
            current_date=TimeUtil.get_current_time(),
        )
        FileUtil.create_new_file(self.__filepath, Data.HEADER)
        return self.__filepath

    def get_data_from_file(self):
        return FileUtil.get_content(self.__filepath)

    def update(self, data) -> None:
        if self.__filepath is not None:
            FileUtil.clear_data(self.__filepath)

            # last row is always empty, let's remove it
            cleaned_data = [row for row in data if any(cell.strip() for cell in row)]

            FileUtil.update_data(self.__filepath, cleaned_data)

    def reset(self):
        self.__filepath = None

    def set_readonly(self):
        if self.__filepath is not None:
            FileUtil.set_readonly(self.__filepath)

