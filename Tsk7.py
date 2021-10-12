x = int(input('Введите число x'))
y = int(input('Введите число y'))
suitable = []
for i in range(x, y):
    if i % 5 == 0:
        suitable.append(i)
print(sum(suitable)) 