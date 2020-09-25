flag = 0
while flag == 0:

    set_1_subset = set(input('Введите числа для подмножества'))
    set_2 = set(input('Введите числа для множества'))
    f_t = set_1_subset.issubset(set_2)
    print(f_t)
    flag = int(input('Для продолжения введите 0, а для выхода любое число'))
