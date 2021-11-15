from collections import Counter


def cntr(list):
    print(Counter(list))


def inptr(lst, inp):
    lst = []
    inp = 0
    while inp != '':
        inp = input('Введите что-нибудь: ')
        lst.append(inp)
    lst = lst[:-1]
    return lst


cntr(inptr(lst=[], inp=0))