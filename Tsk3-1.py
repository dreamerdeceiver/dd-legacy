def inptr(lst, inp):
    lst = []
    inp = 0
    while inp != '':
        inp = input('Введите что-нибудь: ')
        lst.append(inp)
    lst = lst[:-1]
    print(lst)


lst = []
inp = 0
inptr(inp, lst)