#from statistics import mean


def avrg(lst):
    sm = sum(lst) / len(lst)
    print('Среднее арифметическое чисел списка:', sm)


lst = list()
inp = (input('Введите число: '))
while inp != "":
    lst.append(float(inp))
    inp = (input('Введите что-нибудь: '))
print(lst)
avrg(lst)