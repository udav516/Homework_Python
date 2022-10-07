class Person:
    def __init__(self, name, lname, sname, dict_ph):
        self.name = name
        self.lname = lname
        self.sname = sname
        self.dict_ph = dict_ph

    def get_phone(self):
        return dict(self.dict_ph).get('private')

    def get_name(self):
        return f'{self.sname} {self.name} {self.lname}'

    def get_work_phone(self):
        return dict(self.dict_ph).get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.lname}! ' \
               f'Примите участие в нашем беспроигрышном конкурсе для физических лиц.'

class Company:
    def __init__(self, name_c, type_c, dict_cont, *person):
        self.name_c = name_c
        self.type_c = type_c
        self.dict_cont = dict_cont
        self.person_list = list(person)

    def get_phone(self):
        if self.dict_cont.get('contact'):
            return self.dict_cont.get('contact')
        elif not self.dict_cont.get('contact'):
            for i in self.person_list:
                if i.get_work_phone():
                    return i.get_work_phone()
            else:
                return

    def get_name(self):
        return self.name_c

    def get_sms_text(self):
        return f'''Для компании {self.name_c} есть супер предложение! \
Примите участие в нашем беспроигрышном конкурсе для {self.type_c}.'''

def send_sms(*objects):
    for i in objects:
        if i.get_phone():
            print(f'Отправлено СМС на номер {i.get_phone()} c текстом: {i.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {i.get_name()}')

p1 = Person("Ivan", "Ivanovich", "Ivanov", {'private': 123, 'work': 456})
p2 = Person("Ivan", "Peyrovich", "Petrov", {'private': 789})
p3 = Person("Ivan", "Peyrovich", "Sidorov", {'work': 789})
p4 = Person("John", "Unknown", "Doe", {})
c1 = Company("Bell", "OOO", {'contact': 111}, p3, p4)
c2 = Company("Cell", "AO", {"non_contact": 222}, p2, p3)
c3 = Company("Dell", "Ltd", {"non_contact": 333}, p2, p4)
send_sms(p1, p2, p3, p4, c1, c2, c3)

# p1 = Person("Степан", "Петрович", "Джобсов", {'private': 555})
# p2 = Person("Боря", "Иванович", "Гейтсов", {'private': 777, 'work': 888})
# p3 = Person("Семён", "Петрович", "Возняцский", {'work': 789})
# p4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
# c1 = Company("Яблочный комбинат", "OOO", {'contact': 111}, p1, p3)
# c2 = Company("ПластОкно", "AO", {"non_contact": 222}, p2)
# c3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, p4)
# send_sms(p1, p2, p3, p4, c1, c2, c3)
