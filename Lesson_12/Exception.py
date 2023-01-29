from datetime import datetime


class MyCustomException(Exception):

    def __init__(self):
        print('Custom exception is occured')
        with open(file='error.txt', mode='a', encoding='utf-8') as log:
            log.write(f'The error was happened at {datetime.now()}\n')


raise MyCustomException
