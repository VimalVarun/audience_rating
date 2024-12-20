import sys
from src.logger import logging  # Importing your logging configuration

def error_message_detail(error, error_detail: sys):
    try:
        _, _, exc_tb = error_detail.exc_info()  # Retrieve exception details
        file_name = exc_tb.tb_frame.f_code.co_filename  # File name where the error occurred
        line_number = exc_tb.tb_lineno  # Line number of the error
        error_message = (
            f"Error occurred in python script name [{file_name}] "
            f"line number [{line_number}] error message [{str(error)}]"
        )
        return error_message
    except Exception as inner_error:
        return f"Failed to retrieve error details: {inner_error}"

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message




