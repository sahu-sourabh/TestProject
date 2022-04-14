# 6.1 of Documentation

import logging


class LogGen:
    @staticmethod
    def loggen():       # Not Working
        logging.basicConfig(filename='Logs/automation.log',
                            format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def loggen1():      # Working
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(filename='Logs/mylog.log', mode='a')
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
