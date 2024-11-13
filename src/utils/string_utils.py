import re


class StringUtils:

    @staticmethod
    def is_empty(string: str) -> bool:
        return True if len(string) == 0 else False

    @staticmethod
    def is_filename_friendly_character(value: str) -> bool:
        pattern = r'^[\w]+$'
        return bool(re.fullmatch(pattern, value))

    @staticmethod
    def is_letter(value: str) -> bool:
        pattern = r'^[A-Za-z]+$'
        return bool(re.fullmatch(pattern, value))

    @staticmethod
    def is_digit(value: str) -> bool:
        pattern = r'^\d+$'
        return bool(re.fullmatch(pattern, value))

    @staticmethod
    def is_invalid_initials(string: str) -> bool:
        return not (2 <= len(string) <= 3)