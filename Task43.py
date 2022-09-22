# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
# *Пример: *
# [1, 2, 3, 5, 1, 5, 3, 10] = > [2, 10]

initList = [1, 2, 3, 5, 1, 5, 3, 10]

resultList = []
for i in range(len(initList)):
    count = True
    for j in range(0, i):
        if initList[i] == initList[j]:
            count = False
    for j in range(i+1, len(initList)):
        if initList[i] == initList[j]:
            count = False
    if count:
        resultList.append(initList[i])

print(resultList)
