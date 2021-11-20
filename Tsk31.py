def inptr(lst, inp):
    lst = []
    inp = input('Введите что-нибудь: ')
    while inp != '': 
        lst.append(int(inp))
        inp = input('Введите что-нибудь: ')
    return lst


#print(inptr(lst=[], inp=0))