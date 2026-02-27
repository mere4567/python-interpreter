class CustomException(Exception):
    """Base class for other exceptions."""
    pass

class ValidationError(CustomException):
    """Raised when a validation error occurs."""
    pass

class NotFoundError(CustomException):
    """Raised when an item is not found."""
    pass

class PermissionDeniedError(CustomException):
    """Raised when permission is denied."""
    pass

class DatabaseError(CustomException):
    """Raised for database-related errors."""
    pass
