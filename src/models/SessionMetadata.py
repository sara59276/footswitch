from typing import List


class SessionMetadata:
    def __init__(
            self,
            current_date: str = None,
            session_start: str = None,
            session_end: str = None,
            scan_id: str = None,
            animal_id: str = None,
            experimenter_initials: str = None,

    ):
        if (current_date is not None
            and session_start is not None
            and scan_id is not None
            and animal_id is not None
            and experimenter_initials is not None
        ):
            self.__date = current_date
            self.__session_start = session_start
            self.__session_end = session_end
            self.__scan_id = scan_id
            self.__animal_id = animal_id
            self.__experimenter_initials = experimenter_initials

    def get_date(self) -> str:
        return self.__date

    def get_session_start(self) -> str:
        return self.__session_start

    def get_session_end(self) -> str:
        return self.__session_end

    def get_scan_id(self) -> str:
        return self.__scan_id

    def get_animal_id(self) -> str:
        return self.__animal_id

    def get_experimenter_initials(self) -> str:
        return self.__experimenter_initials

    def set_session_end(self, session_end):
        self.__session_end = session_end

    def convert_to_csv(self) -> List[List[str]]:
        return [
            ['date', self.get_date(), ''],
            ['start_measures', self.get_session_start(), ''],
            ['end_measures', self.get_session_end(), ''],
            ['scan_id', self.get_scan_id(), ''],
            ['animal_id', self.get_animal_id(), ''],
            ['experimenter_initials', self.get_experimenter_initials(), ''],
        ]