class RepositoryException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)