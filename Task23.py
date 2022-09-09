# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

N = int(input("Enter array size:"))
numbers = []
result = []
for i in range(N):
    numbers.append(random.randint(-N, N))
for i in range((len(numbers) + 1)//2):
    result.append(numbers[i] * numbers[N - 1 - i])
print(numbers)
print(result)
