def fibonacci(k):
    if k == 1:
        print(1, end=' ')
        return (k, 0)
    else:
        i, j = fibonacci(k - 1)
        print(i + j, end=' ')
        return (i + j, i)


fibonacci(int(input('Введите, сколько чисел нужно отобразить: ')))