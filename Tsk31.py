def inptr(lst, inp):
    lst = list()
    while inp != '': 
        lst.append(int(inp))
        inp = input('Введите что-нибудь: ')
    return lst