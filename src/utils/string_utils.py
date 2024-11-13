class StringUtils:

    @staticmethod
    def is_empty(string: str) -> bool:
        return True if len(string) == 0 else False

    @staticmethod
    def is_invalid_initials(string: str) -> bool:
        return not (2 <= len(string) <= 3)