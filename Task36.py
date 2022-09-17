# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.

file_intText = 'text_input.txt'
file_result = 'text_output.txt'

def read_text(file):
    with open(str(file), 'r', encoding="utf-8") as data:
        tex = data.read()
    return tex

def del_text(pos):
    text = list(filter(lambda x: 'абв' not in x, pos.split()))
    return ' '.join(text)

def write_to_file(file, pos):
    with open(file, 'w', encoding="utf-8") as data:
        data.write(pos)

pos1 = read_text(file_intText)
pos_del = del_text(pos1)
write_to_file(file_result, pos_del)
