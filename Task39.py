# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

file_intText = 'text_input.txt'
file_result = 'text_output.txt'

def read_text(file):
    with open(str(file), 'r', encoding="utf-8") as data:
        tex = data.read()
    return tex

def cod_text(pos):
    coding = ""
    i = 0
    while i < len(pos):
        count = 1
        while i + 1 < len(pos) and pos[i] == pos[i + 1]:
            count += 1
            i += 1
        coding += str(count) + pos[i]
        i += 1
    return coding

def write_to_file(file, pos):
    with open(file, 'w', encoding="utf-8") as data:
        data.write(pos)

pos1 = read_text(file_intText)
pos_cod = cod_text(pos1)
write_to_file(file_result, pos_cod)
