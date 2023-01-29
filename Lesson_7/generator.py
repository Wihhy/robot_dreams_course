n = int(input('What number would you like to get? '))


def fibo(num=n):
    a, b = 1, 1
    for i in range(num):
        yield a
        a, b = b, a + b


print(list(fibo(n))[-1])
