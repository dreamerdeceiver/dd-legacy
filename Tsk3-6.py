from math import sqrt

def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d <= sqrt(a):
        d += 2
    return True

print(is_prime(int(input("Введите число: "))))