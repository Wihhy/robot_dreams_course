# n = int(input())


def fibo(n):
    result = 1
    if n > 2:
        result = fibo(n-1) + fibo(n-2)
    return result


print(fibo(100))
