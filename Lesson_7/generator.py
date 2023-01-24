# n = int(input())


def fibo(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(list(fibo(1000)))
