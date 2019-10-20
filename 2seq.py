# '5,8,9;3,4,6/5,3;3,9'
user_input = input('Введите цифры для формирования списка: ')

# Меняем все разделители на ','
user_input = user_input.replace(';', ',')
user_input = user_input.replace('/', ',')

my_list = []
new_list = []
my_list = user_input.split(',')

for element in my_list:
    count_entries = my_1list.count(element)
    if count_entries == 1:
        new_list.append(element)

print(new_list)