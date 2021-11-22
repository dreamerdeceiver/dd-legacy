def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d ** 2 <= n and n % d != 0:
        d += 2
    return d ** 2 > n


print(isPrime(n=int(input('Введите число: '))))