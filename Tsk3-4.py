from collections import Counter


def cntr(lst):
    print(Counter(lst))


lst = list()
inp = (input('Введите число: '))
while inp != '':
    lst.append(inp)
    inp = (input('Введите что-нибудь: '))
cntr(lst)