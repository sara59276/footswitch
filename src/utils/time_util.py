from datetime import datetime, time


class TimeUtil:

    @staticmethod
    def get_current_date() -> datetime:
        return datetime.now()

    @staticmethod
    def get_current_time() -> time:
        return datetime.now().time()

    @staticmethod
    def get_formatted_current_date(date_format: str = "%Y-%m-%d") -> str:
        return TimeUtil.get_current_date().strftime(date_format)

    @staticmethod
    def get_formatted_current_time(time_format: str = "%H:%M:%S.%f", msec_digits: int = 2) -> str:
        if not 0 <= msec_digits <= 6:
            raise ValueError("msec_digits must be between 0 and 6")

        return TimeUtil.get_current_time().strftime(time_format)[:-(6-msec_digits)]
