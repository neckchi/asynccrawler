import logging
import os
from datetime import datetime


class LoggerFactory(object):
    _LOG = None

    @staticmethod
    def __create_logger(log_file, log_level):
        """
        A private method that interacts with the python
        logging module
        """
        # set the logging format
        log_format = "%(asctime)s:%(levelname)s:%(message)s"

        # Initialize the class variable with logger object
        log_file_name = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), f'../logger_factory/logs/service_loop_{datetime.now().strftime("%Y%m%d")}.log')
        LoggerFactory._LOG = logging.getLogger(log_file)
        logging.basicConfig(filename=log_file_name, level=logging.INFO,
                            format=log_format, datefmt="%Y-%m-%d %H:%M:%S")
        # set the logging level based on the user selection
        if log_level == "INFO":
            LoggerFactory._LOG.setLevel(logging.INFO)
        elif log_level == "ERROR":
            LoggerFactory._LOG.setLevel(logging.ERROR)
        elif log_level == "DEBUG":
            LoggerFactory._LOG.setLevel(logging.DEBUG)
        return LoggerFactory._LOG

    @staticmethod
    def get_logger(log_file, log_level):
        """
        A static method called by other modules to initialize logger in
        their own module
        """
        logger = LoggerFactory.__create_logger(log_file, log_level)
        # return the logger object
        return logger
