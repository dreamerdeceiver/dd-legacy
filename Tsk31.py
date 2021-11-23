def inptr(lst):
    lst = list()
    inp = input('Введите что-нибудь: ')
    while inp != '': 
        lst.append(int(inp))
        inp = input('Введите что-нибудь: ')
    return lst