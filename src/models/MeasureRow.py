from datetime import time
from typing import Optional


class MeasureRow:
    def __init__(self):
        self.__event: Optional[str] = None
        self.__start_time: Optional[time] = None
        self.__end_time: Optional[time] = None

    def get_event(self) -> str:
        return self.__event

    def set_event(self, event) -> None:
        self.__event = event

    def get_start_datetime(self) -> time:
        return self.__start_time

    def set_start_datetime(self, start_datetime) -> None:
        self.__start_time = start_datetime

    def get_end_datetime(self) -> time:
        return self.__end_time

    def set_end_datetime(self, end_datetime) -> None:
        self.__end_time = end_datetime

    def get_row(self) -> list[str]:
        return [
            self.__event,
            self.__start_time,
            self.__end_time
        ]