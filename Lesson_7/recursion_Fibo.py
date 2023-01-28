n = int(input('What number would you like to get? '))


def fibo(num=n):
    result = 1
    if num > 2:
        result = fibo(num-1) + fibo(num-2)
    return result


print(fibo(n))
