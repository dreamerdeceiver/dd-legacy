from Tsk31 import inptr


def sttr(x):
    if len(set(x)) == len(x):
        return True
    else:
        return False


assert sttr([1, 2, 3, 3, 4]) == False
assert sttr([1, 2, 3, 4, 5]) == True
print(sttr(inptr(lst=[], inp=input('Введите что-нибудь: ' ))))