from Tsk31 import inptr


def shftr(lst, n):
    if n != 0:
        return lst[-n:] + lst[:-n]
    else:
        return lst

assert shftr([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
assert shftr([1, 2, 3, 4, 5], 4) == [2, 3, 4, 5, 1]
assert shftr([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
print(shftr(inptr(lst=[], inp=input('Введите что-нибудь: ')), n=int(input('На сколько позиций сдвинуть: '))))