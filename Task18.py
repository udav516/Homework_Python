# Реализуйте алгоритм перемешивания списка.
import random

N = int(input("Enter array size:"))
numbers = []
for i in range(N):
    numbers.append(random.randint(-10, 10))
print(numbers)
random.shuffle(numbers)
print(numbers)
