import inspect

import pytest
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filhandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filhandler.setFormatter(formatter)
        logger.addHandler(filhandler)
        logger.setLevel(logging.DEBUG)
        return logger
