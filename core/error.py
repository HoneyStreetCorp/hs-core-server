from dto.error.error_response import ErrorResponse


class CustomException(Exception):
    def __init__(self, error_response: ErrorResponse):
        self.error_response = error_response
