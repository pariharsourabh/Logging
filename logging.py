import logging

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper
