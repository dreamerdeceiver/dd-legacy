X = float(input('Введите координату X'))
Y = float(input('Введите координату Y'))
if X > 0 and Y > 0:
    print('Точка принадлежит первой четверти')
elif X < 0 and Y > 0:
    print('Точка принадлежит второй четверти')
elif X < 0 and Y < 0:
    print('Точка принадлежит третей четверти')
elif X > 0 and Y < 0:
    print('Точка принадлежит четвёртой четверти')
elif X == 0 and Y != 0:
    print('Точка лежит на оси X')
elif Y == 0 and X != 0:
    print('Точка лежит на оси Y')
else: 
    print('Точка попадает в начало координат') 