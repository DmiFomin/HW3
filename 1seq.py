count_elements = input('Введите кол-во элементов списка: ')

# Проверка на ввод числа
if count_elements.isdigit():
    i = 0
    my_list = []
    while i < int(count_elements):
        current_element = ''
        while not current_element.isdigit():
            current_element =  input(f'Введите {i+1} элемент: ')
            if  not current_element.isdigit():
                print('Нужно ввести число!')

        my_list.append(current_element)
        i = i + 1

    my_list.sort()
    print(my_list)

else:
    print('Нужно ввести число!')

print('The End')