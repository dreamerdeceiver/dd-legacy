from random import randint

n = randint(0, 100)
tr = int(input('Введите число: '))
while True:
    if tr < n:
        print('Загаданное число больше введённого')
        tr = int(input('Введите число: '))
    elif tr > n:
        print('Загаданное число меньше введённого')
        tr = int(input('Введите число: '))
    else:
        print('В точку!')
        break
print('Вы угадали число!')