

def search(user_list):
    request = input('Введите имя, фамилию или телефон: ')
    temp = ''
    t = True
    for i in user_list:
        if i['LastName'] == request or i['Name'] == request or i['Number'] == request:
            print(*i.values())
            temp = i.values()
            t = False
    if t:
        print('Нет такого usera')
    return ' '.join(temp)
