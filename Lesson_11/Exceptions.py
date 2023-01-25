import datetime


class MyCustomException(Exception):

    def __init__(self):
        print('Custom exception is occured')


class Selection:

    def __init__(self):
        pass

    def __enter__(self):
        print('==========')
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('==========')


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

print()

try:
    print('Before exception')
    raise MyCustomException
except MyCustomException:
    print('After exception')

print()

with Selection():
    print('Select it')
