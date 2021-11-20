from Tsk31 import inptr

def avrg(list):
    if len(list) != 0:
        sm = sum(list) / len(list)
        print('Среднее арифметическое чисел списка:', sm)
    else:
        print('Введён пустой список')


avrg(inptr(lst=[], inp=0))