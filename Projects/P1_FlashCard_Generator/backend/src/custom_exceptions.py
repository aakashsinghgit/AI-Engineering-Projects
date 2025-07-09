import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys) -> str:
    """
    Generates a detailed error message from the exception and its context.
    
    Args:
        error (Exception): The exception that occurred.
        error_detail (sys): The sys module to access exception details.
    
    Returns:
        str: A formatted error message with type, value, and traceback.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception class to handle exceptions with detailed logging.
    
    Args:
        error (Exception): The exception that occurred.
        error_detail (sys): The sys module to access exception details.
    """
    def __init__(self, error, error_detail: sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         a = 1 / 0  # Example to raise an exception
#     except Exception as e:
#         logging.error("Divide by zero exception occurred")
#         raise CustomException(e, sys) from e