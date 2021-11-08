list = [] 
inp = 0
while True:
    if inp != '':
        inp = input('Введите что-нибудь: ')
        list.append(inp)
    else:
        break
print(list)