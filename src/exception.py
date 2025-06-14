import sys

def detailed_ex_message(error_message,error_detail:sys):
    _,_,exec_tb=error_detail.exc_info() #current exception's traceback object
    file_name=exec_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exec_tb.tb_lineno,str(error_message)
    )
    return error_message

class custom_exception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=detailed_ex_message(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

