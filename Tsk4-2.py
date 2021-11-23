def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


assert fac(9) == 362880
assert fac(17) == 355687428096000
print(fac(n=int(input('Введите число: '))))