import re

string = input('Введите что-нибудь ')
x = re.findall('(\d+)', string)
print(x[int(input('Введите индекс числа в строке: ')) - 1])