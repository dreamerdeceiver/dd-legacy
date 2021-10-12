a = int(input('Введите число'))
b = int(input('Введите число'))
c = int(input('Введите число'))
d = int(input('Введите число'))
f = int(input('Введите число'))
head = a * b - c
fndtn = f - d 
if fndtn == 0:
    print('Делить на ноль нельзя!')
else:
    ans = head / fndtn
    print(ans)