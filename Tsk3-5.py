def avrg(list):
    sm = sum(list) / len(list)
    print('Среднее арифметическое чисел списка:', sm)


def inptr(lst, inp):
    lst = []
    inp = input('Введите что-нибудь: ')
    while inp != '': 
            lst.append(int(inp))
            inp = input('Введите что-нибудь: ')
    return lst 
    
    
avrg(inptr(lst=0, inp=0))