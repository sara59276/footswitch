from datetime import datetime, time


class TimeUtil:

    @staticmethod
    def get_current_year_month_day() -> tuple[str, str, str]:
        today = TimeUtil.get_current_date()
        return today.strftime("%Y"), today.strftime("%m"), today.strftime("%d")

    @staticmethod
    def get_current_date() -> datetime:
        return datetime.now()

    @staticmethod
    def get_formatted_current_date(date_format: str = "%Y-%m-%d") -> str:
        return TimeUtil.get_current_date().strftime(date_format)

    @staticmethod
    def get_current_time() -> time:
        return datetime.now().time()

    @staticmethod
    def get_formatted_current_time(
            time_format: str = "%H:%M:%S.%f",
            msec_digits: int = 2,
    ) -> str:
        current_time = TimeUtil.get_current_time()
        return TimeUtil.format_time(current_time, time_format, msec_digits)

    @staticmethod
    def get_midpoint_time(
            start_datetime: datetime,
            end_datetime: datetime,
    ) -> time:
        return (start_datetime + (end_datetime - start_datetime) / 2).time()

    @staticmethod
    def get_formatted_midpoint_time(start_datetime: datetime, end_datetime) -> str:
        midpoint_time = TimeUtil.get_midpoint_time(start_datetime, end_datetime)
        return TimeUtil.format_time(midpoint_time)

    @staticmethod
    def format_time(
            time_obj: time,
            time_format: str = "%H:%M:%S.%f",
            msec_digits: int = 2,
    ) -> str:
        if not 0 <= msec_digits <= 6:
            raise ValueError("msec_digits must be between 0 and 6")

        formatted_time = time_obj.strftime(time_format)

        if msec_digits == 0:
            return formatted_time[:8]
        else:
            return formatted_time[:-(6 - msec_digits)]