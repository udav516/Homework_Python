import log

def data_add():
    f = open('data.txt', 'a', encoding="utf-8")
    user_list = input('Введите данные через пробел: ')
    f.writelines(f'\n{user_list}')
    f.close()
    log.log_add(user_list)


