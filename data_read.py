def read_pol(file):
    with open(str(file), 'r', encoding="utf-8") as data:
        pol = data.readlines()
    return pol
