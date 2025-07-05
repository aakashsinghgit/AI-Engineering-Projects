import sys
from src.logger import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Returns a detailed error message including file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
        f"Error occurred in script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"with message: [{str(error)}]"
    )
    return error_message

class CustomException(Exception):
    """
    Custom exception class to handle exceptions with detailed error messages.
    """
    def __init__(self, error: Exception, error_detail: sys):
        message = error_message_detail(error, error_detail)
        super().__init__(message)
        self.error_message = message
        # Optional: log the error message immediately
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message

# Example usage:
if __name__ == "__main__":
    try:
        a = 1 / 0  # Example to raise an exception
    except Exception as e:
        logging.info("Divide by zero exception occurred")
        raise CustomException(e, sys) from e
