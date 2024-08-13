import sys
import time
import logging
from logging.handlers import RotatingFileHandler
from typing import Any, Callable

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(
    'logger.log',
    maxBytes=50000000,
    backupCount=5,
    encoding='utf-8'
)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

def logger_decorator(func):
    """
    Decorator for logging both in the file 'logger.log' and in the console.
    """
    def wrapper(*args, **kwargs):
        try:
            logger.debug('Starting function')
            result = func(*args, **kwargs)
            logger.debug('Ending function')
        except Exception as error:
            logger.error(f'{error}')
            return f'An error occured: {error}'
        return result

    return wrapper


@logger_decorator
def counter(count: int) -> dict:
    """
    Dictionary with multiplication tables.
    """
    time.sleep(1)
    return {i: i ** 2 for i in range(count)}


if __name__ == '__main__':
    size: int = int(input())
    counter(size)
