# Task 1: Writing and Testing a Decorator
# one-time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(
            logging.INFO,
            f"positional parameters: {list(args) if args else 'none'}"
        )
        logger.log(
            logging.INFO,
            f"keyword parameters: {kwargs if kwargs else 'none'}"
        )
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def positional_func(*args):
    return True

@logger_decorator
def keyword_func(**kwargs):
    return logger_decorator
if __name__ == "__main__":
    hello_world()
    positional_func(1, 2, 3)
    keyword_func(a=10, b=20)