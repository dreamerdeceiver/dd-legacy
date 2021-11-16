def avrg(list):
    sm = sum(list) / len(list)
    print('Среднее арифметическое чисел списка:', sm)


def inptr(lst, inp):
    lst = []
    inp = int(input('Введите что-нибудь: '))
    while inp != '': 
        try:
            lst.append(inp)
            inp = int(input('Введите что-нибудь: '))
        except:
            return lst
    return lst 
    
    
avrg(inptr(lst=0, inp=0))