from Tsk31 import inptr

def avrg(list):
    if len(list) != 0:
        sm = sum(list) / len(list)
        return sm
    else:
        return "Введён пустой список"


print(avrg(inptr(lst=[], inp=input('Введите что-нибудь: '))))