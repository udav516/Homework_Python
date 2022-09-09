# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

N = int(input("Enter array size:"))
numbers = []
summ = 0
for i in range(N):
    numbers.append(random.randint(0, 9))
    if i % 2 != 0:
        summ += numbers[i]
print(numbers)
print(summ)
