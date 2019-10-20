# 5,8,9;3,4,6/5,3;3,9
# 3,5/8

user_input_source_list = input('Введите цифры для формирования исходного списка: ')
user_input_del_list = input('Введите цифры для формирования списка для удаления: ')

source_list = user_input_source_list.replace(';', ',').replace('/', ',').split(',')
del_list = user_input_del_list.replace(';', ',').replace('/', ',').split(',')

print(f'Исходный список: {source_list}')
print(f'Список для удаления: {del_list}')

for element in del_list:
    while (element in source_list):
        source_list.remove(element)

print(f'Исходный список после удаления {source_list}')
