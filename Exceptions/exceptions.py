class InvalidDataException(Exception):
    def __init__(self, message="Invalid data provided."):
        super().__init__(message)

class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock available."):
        super().__init__(message)

class IncompleteOrderException(Exception):
    def __init__(self, message="Order details are incomplete."):
        super().__init__(message)

class PaymentFailedException(Exception):
    def __init__(self, message="Payment processing failed."):
        super().__init__(message)

class IOException(Exception):
    def __init__(self, message="An I/O error occurred while writing to the file."):
        super().__init__(message)

class SqlException(Exception):
    def __init__(self, message="Database error occurred."):
        super().__init__(message)

class ConcurrencyException(Exception):
    def __init__(self, message="Data conflict detected during concurrent update."):
        super().__init__(message)

class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed. User not logged in."):
        super().__init__(message)

class AuthorizationException(Exception):
    def __init__(self, message="Unauthorized access attempt detected."):
        super().__init__(message)


