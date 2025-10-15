import sys
class CustomException(Exception):
    def __init__(self,message:str,error_detail: Exception=None):
        self.error_message=self.get_detailed_error_message(message,error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        """Format the error message with traceback details."""
        _,_,exc_tb=sys.exc_info()
        line_number=exc_tb.tb_lineno
        file_name=exc_tb.tb_frame.f_code.co_filename
        error_message=f"Error occurred in script: {file_name} at line number: {line_number} with message: {message}"
        return error_message    
    
    def __str__(self):
        return self.error_message