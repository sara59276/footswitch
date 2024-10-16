from constants.layout_configurations import TIME_LIMIT_SECONDS


class Timer:
    def __init__(self):
        self.__seconds = 0
        self.__threashold_seconds = TIME_LIMIT_SECONDS

    def update(self):
        self.__seconds += 1

    def is_threashold_attained(self) -> bool:
        return self.__seconds >= self.__threashold_seconds