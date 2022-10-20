
import logging
import sys
from enum import Enum
from pathlib import Path

# formatting options: https://docs.python.org/3/library/logging.html#logrecord-attributes
# this template of printing logs & saving to file in parallel based on: https://stackoverflow.com/questions/61141419/in-python-i-can-write-a-log-to-console-but-its-not-getting-written-into-file

import logging


class Color:
    """A class for terminal color codes."""

    BOLD = "\033[1m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    BOLD_WHITE = BOLD + WHITE
    BOLD_BLUE = BOLD + BLUE
    BOLD_GREEN = BOLD + GREEN
    BOLD_YELLOW = BOLD + YELLOW
    BOLD_RED = BOLD + RED
    BOLD_CYAN = BOLD + CYAN
    BOLD_MAGENTA = BOLD + MAGENTA
    BOLD_BLUE = BOLD + BLUE
    END = "\033[0m"


class ColorLogFormatter(logging.Formatter):
    """
    A class for formatting colored logs.
    Based on : https://stackoverflow.com/a/70796089

    """
    #%(pathname)s
    FORMAT = "%(prefix)s%(asctime)s - %(name)s - %(levelname)s - line %(lineno)d - %(message)s%(suffix)s"

    LOG_LEVEL_COLOR = {
        "DEBUG": {'prefix': Color.CYAN, 'suffix': Color.END},
        "INFO": {'prefix': Color.MAGENTA, 'suffix': Color.END},
        "WARNING": {'prefix': Color.YELLOW, 'suffix': Color.END},
        "ERROR": {'prefix': Color.RED, 'suffix': Color.END},
        "CRITICAL": {'prefix': Color.RED, 'suffix': Color.END},
    }

    def format(self, record):
        """Format log records with a default prefix and suffix to terminal color codes that corresponds to the log level name."""
        if not hasattr(record, 'prefix'):
            record.prefix = self.LOG_LEVEL_COLOR.get(
                record.levelname.upper()).get('prefix')

        if not hasattr(record, 'suffix'):
            record.suffix = self.LOG_LEVEL_COLOR.get(
                record.levelname.upper()).get('suffix')

        formatter = logging.Formatter(self.FORMAT)
        return formatter.format(record)


class LoggingLevels(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class Logger:
    def __init__(self, loggerName, logFileName, loggingLevel = 'DEBUG') -> None:

        self.loggerName = loggerName
        self.logFileName = logFileName

        try:
            self.loggingLevel = LoggingLevels[loggingLevel].value
        except:
            self.loggingLevel = 'DEBUG'
            

        self.logger = logging.Logger(self.loggerName)

        # Stream/console output - handle logging settings for console printing
        self.logger.handler = logging.StreamHandler(sys.stdout)
        self.logger.handler.setLevel(self.loggingLevel)
        self.logger.handler.setFormatter(ColorLogFormatter())
        self.logger.addHandler(self.logger.handler)

        # File output - handle logging settings for log file saving
        fh = logging.FileHandler(f"{self.logFileName}.log")
        fh.setLevel(self.loggingLevel)
        fh.setFormatter(logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - line %(lineno)d - %(message)s"))
        self.logger.addHandler(fh)

    def __str__(self) -> str:
        # use: print(log)
        return 'This class intendet to use as a general purpose logger'

    def __call__(self, *args, **kwds):
        # use: log()
        print('ok ok...')

    def setLoggerName(self, name):
        self.logger.name = name



###########################
# initiate logger example #
###########################

# logger = Logger(logFileName='test', loggerName=Path(sys.argv[0]).parts[-1], loggingLevel='DEBUG')

# overwrite default colors
#logger.logger.warning('dsaa', extra={'prefix': Color.GREEN, 'suffix': Color.END})

# just examples of different levels
# logger.logger.debug('dsaa')
# logger.logger.info('dsaa')
# logger.logger.warning('dsaa')
# logger.logger.error('dsaa')
# logger.logger.critical('dsaa')


# print(logger.handlers)
