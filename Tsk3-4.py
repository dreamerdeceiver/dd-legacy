from collections import Counter


def cntr(lst, inp):
    lst = []
    inp = 0
    while True:
        if inp != '':
            inp = input('Введите что-нибудь: ')
            lst.append(inp)
        else:
            break
        new_lst = lst[:-1]
    print(Counter(new_lst))


lst = []
inp = 0
cntr(lst, inp)