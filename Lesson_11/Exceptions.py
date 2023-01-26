import datetime


def name_and_time(input_func):
    def inside_func():
        print(f'The function "{input_func.__name__}" was called at {datetime.datetime.now()}')
        input_func()

    return inside_func


@name_and_time
def printik():
    print('Im inside the function')


printik()

print()


class MyCustomException(Exception):

    def __init__(self):
        print('Custom exception is occured')


try:
    print('Before exception')
    raise MyCustomException
except MyCustomException:
    print('After exception')

print()


class Selection:

    def __init__(self):
        pass

    def __enter__(self):
        print('==========')
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('==========')


with Selection():
    print('Select it')

print()

try:
    print('=' * 10)
    print('Doing something very important')
except Exception as exc:
    print(exc)
finally:
    print('=' * 10)

print()

with Selection() as select:
    print('important')
