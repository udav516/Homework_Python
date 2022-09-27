
def record_input(file):
    user_list = []
    for i in file:
        raw_test = i.split()
        user_data = {'LastName': raw_test[0], 'Name': raw_test[1], 'Number': raw_test[2]}
        user_list.append(user_data)
    return user_list
