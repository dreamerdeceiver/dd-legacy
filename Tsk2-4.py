string = input('Введите что-нибудь')
qty1 = string.count('(')
qty2 = string.count(')')
diff1 = qty1 - qty2
diff2 = qty2 - qty1
if qty1 > qty2:
    print('Не хватает', diff1, 'открывающих скобок')
elif qty2 > qty1:
    print('Не хватает', diff2, 'закрывающих скобок')
else:
    print('Количество открывающих скобок соответствует количеству закрывающих')