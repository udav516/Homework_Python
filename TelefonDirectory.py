# Разделим сервис на этапы:
# 1.Как можно вводить данные?
# ‘Фамилия Имя Номер’
# 2.Как их обрабатывать? Где хранить?
# user = {‘Name’:’’, ‘Last Name’:’’, ‘number’:’’ }
# user_list = [user1,user2,user3……]
# 3.Как запрашивать и получать данные?
# 4.Какие функции можно для этого создать?
# 5.Как вынести функции в модули?
from data_read import *
from data_output_record import *
from data_search import *
from data_add import *

file_int = 'data_input.txt'
file_out = 'data_output.txt'

pos1 = read_pol(file_int)
pos2 = search(record_input(pos1))
print(write_to_file(file_out, pos2))



