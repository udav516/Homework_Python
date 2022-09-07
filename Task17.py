# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

N = int(input("Enter array size:"))
numbers = []
for i in range(N):
    numbers.append(random.randint(-N, N))
count = 1
with open('numbers.txt', 'r') as f:
    for i in f:
        print(i)
        count = count * numbers[int(i)]
print(count)
