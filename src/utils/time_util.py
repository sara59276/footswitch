from datetime import datetime


class TimeUtil:

    @staticmethod
    def get_current_date():
        return datetime.now().strftime("%Y%m%d")

    @staticmethod
    def get_current_time():
        return datetime.now().time().strftime("%H:%M:%S.%f")
