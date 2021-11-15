def avrg(list):
    sm = sum(list) / len(list)
    print('Среднее арифметическое чисел списка:', sm)


def inptr(lst, inp):
    lst = []
    inp = 0
    while inp != '':
        inp = input('Введите что-нибудь: ')
        lst.append(inp)
    lst = lst[:-1]
    return lst


avrg(inptr(lst=0, inp=0))
#lst = [2, 4, 6 ,8]
#avrg(lst)