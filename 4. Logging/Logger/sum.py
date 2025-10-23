from logger import logging

def sum(a,b):
    logging.debug("Entered into the funciton")
    return a + b


result = sum(3,4)

logging.debug("Operation Successfully Executed")