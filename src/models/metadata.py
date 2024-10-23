from typing import List

from repo.repository import FileRepository
from utils.time_util import TimeUtil


class Metadata:

    def __init__(
            self,
            current_date: str = "",
            session_start: str = "",
            session_end: str = "",
            scan_id: str = "",
            animal_id: str = "",
            experimenter_initials: str = "",
    ):
        self.__date = current_date
        self.__session_start = session_start
        self.__session_end = session_end
        self.__scan_id = scan_id
        self.__animal_id = animal_id
        self.__experimenter_initials = experimenter_initials

        self.__repo = FileRepository()

    def set_start_session_attributes(
            self,
            current_date: str,
            session_start: str,
            scan_id: str,
            animal_id: str,
            experimenter_initials: str,
    ) -> None:
        self.__date = current_date
        self.__session_start = session_start
        self.__scan_id = scan_id
        self.__animal_id = animal_id
        self.__experimenter_initials = experimenter_initials

    def set_session_end(self) -> None:
        self.__session_end = TimeUtil.get_current_time()
        # TODO màj du fichier quand on set end session

    def convert_to_csv(self) -> List[List[str]]:
        return [
            ['date', self.__date, ''],
            ['session_start', self.__session_start, ''],
            ['session_end', self.__session_end, ''],
            ['scan_id', self.__scan_id, ''],
            ['animal_id', self.__animal_id, ''],
            ['experimenter_initials', self.__experimenter_initials, ''],
            ['','',''],
        ]