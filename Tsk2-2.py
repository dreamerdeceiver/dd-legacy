print('Вводите значения, нажимайте enter')
print('для окончания ввода просто нажмите enter')
a = int(input('-->> '))
elts = []
while True:
    try:
        elts.append(a)
        a = int(input('-->> '))
    except:
        break
elts.sort(key=lambda n: str(abs(n))[0], reverse = True)
print(''.join([str(i) for i in elts]))