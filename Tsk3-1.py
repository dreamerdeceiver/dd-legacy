def inptr(lst, inp):
    lst = []
    inp = 0
    while inp != '':
        inp = input('Введите что-нибудь: ')
        lst.append(inp)
    lst = lst[:-1]
    return lst


print(inptr(lst=[], inp=0))