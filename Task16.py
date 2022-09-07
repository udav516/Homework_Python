# Задайте список из n чисел последовательности (1+ 1/ n) ^ n и выведите на экран их сумму.
n = int(input('Enter number: '))
dictionary = 0
sumDict = 0
for i in range(1, n + 1):
    dictionary = (round((1 + 1 / i) ** i, 2))
    sumDict += dictionary
    print(dictionary, end=' ')
print('[', round(sumDict), ']')

