from datetime import datetime, time


class TimeUtil:

    @staticmethod
    def get_current_date() -> datetime:
        return datetime.now()

    @staticmethod
    def get_current_year_month_day() -> tuple[str, str, str]:
        today = TimeUtil.get_current_date()
        return today.strftime("%Y"), today.strftime("%m"), today.strftime("%d")

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

        current_time = TimeUtil.get_current_time()
        formatted_time = current_time.strftime(time_format)

        if msec_digits == 0:
            return formatted_time[:8]
        else:
            return formatted_time[:-(6 - msec_digits)]
