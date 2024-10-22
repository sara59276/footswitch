from typing import List


class SessionMetadata:
    def __init__(
            self,
            current_date: str = None,
            session_start: str = None,
            scan_id: str = None,
            animal_id: str = None,
            experimenter_initials: str = None,

    ):
        self.__date = current_date
        self.__session_start = session_start
        self.__session_end = ""
        self.__scan_id = scan_id
        self.__animal_id = animal_id
        self.__experimenter_initials = experimenter_initials

    def set_session_end(self, session_end):
        self.__session_end = session_end

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