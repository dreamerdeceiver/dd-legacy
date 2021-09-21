X = int(input('Введите число X'))
Y = int(input('Введите число Y'))
suitable = []
for i in range(X , Y):
    if i % 5 == 0:
        suitable.append(i)
print (sum(suitable)) 