# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# F−1 = 1
# F−2 = -1
# Fn = F(n+2)−F(n+1)

n = int(input('Enter number:'))
fib1 = 0
fib2 = 1
array = [0, 1]
for i in range(2, n + 1):
    fib1, fib2 = fib2, fib1 - fib2
    array.append(fib2)
array.reverse()
fib1 = 0
fib2 = 1
array.append(fib2)
for i in range(2, n + 1):
    fib1, fib2 = fib2, fib1 + fib2
    array.append(fib2)
print(array)
