from typing import List
from repositories.repository import FileRepository
from utils.time_util import TimeUtil


class Metadata:

    def __init__(self):
        self.__date = None
        self.__session_start = None
        self.__session_end = None
        self.__scan_id = None
        self.__animal_id = None
        self.__experimenter_initials = None
        self.__delay = None

        self.__repo = FileRepository()

    def set_starting_metadata(
            self,
            filepath: str,
            scan_id: str,
            animal_id: str,
            experimenter_initials: str,
            delay: str,
    ) -> None:
        self.__date = TimeUtil.get_formatted_current_date()
        self.__session_start = TimeUtil.get_formatted_current_time(msec_digits=0)
        self.__session_end = ""
        self.__scan_id = scan_id
        self.__animal_id = animal_id
        self.__experimenter_initials = experimenter_initials
        self.__delay = delay

        self._update_repository(filepath)

    def set_session_end(self, filepath) -> None:
        if not (self.__date
                or self.__session_start
                or self.__session_end
                or self.__scan_id
                or self.__animal_id
                or self.__experimenter_initials
                or self.__delay
        ):
            raise ValueError("Date, Session start, Session and, Scan ID, Animal ID and Experimenter initials should be defined")

        self.__session_end = TimeUtil.get_formatted_current_time(msec_digits=0)
        self._update_repository(filepath)

    def get_session_start(self) -> str:
        return self.__session_start

    def get_session_end(self) -> str:
        return self.__session_end

    def _update_repository(self, filepath):
        self.__repo.overwrite_metadata(filepath, self._get_metadata_converted_for_csv())

    def _get_metadata_converted_for_csv(self) -> List[List[str]]:
        return [
            ['date<Y-m-d>', self.__date],
            ['session_start<H:M:S>', self.__session_start],
            ['session_end<H:M:S>', self.__session_end],
            ['scan_id', self.__scan_id],
            ['animal_id', self.__animal_id],
            ['experimenter_initials', self.__experimenter_initials],
            ['delay', self.__delay],
        ]
