from datetime import datetime


def name_and_time(input_func):
    def inside_func(*args, **kwargs):
        with open('log.txt', mode='a') as log:
            log.write(f'The function "{input_func.__name__}" was called at {datetime.now()}\n')
        return input_func(*args, **kwargs)

    return inside_func


@name_and_time
def printik():
    print('Im inside the function')


printik()
