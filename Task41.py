# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *.приоритет операций стандартный.
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;
# 5 + 4 * 6 / 12 - 4;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример: *
# 1 + 2 * 3 = > 7;
# (1 + 2) * 3 = > 9;
# (5 * (4 + 6) - 2) / 12

some_string = str(input('Введите арифметическое выражение через пробел: ')).split()
list_sings = [some_string[i] for i in range(len(some_string)) if some_string[i] == '*' or some_string[i] == '/' or some_string[i] == '+' or some_string[i] == '-']

def split_into_arfim(some, list):
    sings = []
    numbers = []
    temp = ''
    for i in some:
        if not i in list:
            temp += i
        else:
            sings.append(i)
            numbers.append(int(temp))
            temp = ''
    numbers.append(int(temp))

    while len(numbers) > 1:
        if '*' in sings:
            index = sings.index('*')
            temp = arithmetic(numbers[index], numbers[index + 1], '*')
            numbers[index] = temp
        elif '/' in sings:
            index = sings.index('/')
            temp = arithmetic(numbers[index], numbers[index + 1], '/')
            numbers[index] = temp
        elif '+' in sings:
            index = sings.index('+')
            temp = arithmetic(numbers[index], numbers[index + 1], '+')
            numbers[index] = temp
        elif '-' in sings:
            index = sings.index('-')
            temp = arithmetic(numbers[index], numbers[index + 1], '-')
            numbers[index] = temp
        del (numbers[index + 1])
        del (sings[index])
    return numbers[0]

def arithmetic(x, y, pos):
    if pos == '+':
        return x+y
    if pos == '-':
        return x-y
    if pos == '*':
        return x*y
    if pos == '/':
        return x/y

print(some_string)
print(list_sings)
print(split_into_arfim(some_string, list_sings))

