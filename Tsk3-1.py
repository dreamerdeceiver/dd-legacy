def inptr(lst, inp):
    lst = []
    inp = 0
    while True:
        if inp != '':
            inp = input('Введите что-нибудь: ')
            lst.append(inp)
        else:
            break
        new_lst = lst[:-1]
    print(new_lst)


lst = []
inp = 0
inptr(inp, lst)