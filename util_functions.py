import asyncio
import functools
from logger import logger


def try_times(number_of_tries):
    """
    Decorator for coroutines to try running one 'number_of_tries' times
    Otherwise raise exception
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            current_try = 1
            while current_try <= number_of_tries:
                try:
                    result = await func(*args, **kwargs)
                    return result
                except Exception as exc:
                    logger.warning(f"{current_try=}, waiting {current_try*10=}")
                    logger.exception(exc)
                    await asyncio.sleep(current_try * 10)
                    current_try += 1
            raise Exception("Number of tries exceeded")
        return wrapper
    return decorator