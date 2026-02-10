from .base_exc import NotFoundError, AppException


class NotFoundUserError(NotFoundError):
    def __init__(self, user_id: int = None):
        self.user_id = user_id
        if user_id:
            message = f"User with id {user_id} not found"
        else:
            message = "User not found"
        super().__init__(message)


class DatabaseError(AppException):
    def __init__(self, message: str = "Database operation failed"):
        super().__init__(message, status_code=500)


class DatabaseConnectionError(DatabaseError):
    def __init__(self):
        super().__init__("Failed to connect to database")


class DatabaseIntegrityError(DatabaseError):
    def __init__(self, detail: str = None):
        message = "Database integrity constraint violated"
        if detail:
            message += f": {detail}"
        super().__init__(message)


class ValidationError(AppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=422)


class AlreadyExistsError(AppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=409)
