# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.+
dictionary = ['Маша', 'Коля', 'Даша', 'Юра']

def to_dict(lst):
    dict_data = {}
    for i in lst:
        dict_data.setdefault(i, i)
    return dict_data

print(to_dict(dictionary))