flag_to_exit = 0
while flag_to_exit == 0:
    list_s = list(input('Введите последовательность чисел: \n'))
    len_list = len(list_s)
    max_number_index = 0
    for i in range(0, len_list):
        if list_s[i] > list_s[max_number_index]:
            max_number_index = i
    print('Индекс и значение наибольшего элемента в списке: ', max_number_index, list_s[max_number_index])
    min_number_index = 0
    for i in range(0, len_list):
        if list_s[i] < list_s[min_number_index]:
            min_number_index = i
    print('Индекс и значение наименьшего элемента в списке', min_number_index, list_s[min_number_index])
    list_s[min_number_index], list_s[max_number_index] = list_s[max_number_index], list_s[min_number_index]
    print(list_s)
    #print('Индекс минимального числа в списке ', min_number_index)
    #list_f = list_s[max_number_index], list_s[min_number_index] = list_s[min_number_index], list_s[max_number_index]
    #print('Список с измененным индексом наибольшего и наименьшего чисел\n', list_f)
    exit_to = int(input('Для выхода введите любую цифру, для продолжения введите "0"'))
    flag_to_exit = exit_to
