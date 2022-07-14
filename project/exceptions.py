class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404


class UserAlreadyExists(Exception):
    pass


class IncorrectPassword(Exception):
    pass


class InvalidToken(Exception):
    pass
