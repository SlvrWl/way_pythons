flag_exit = 0
while flag_exit == 0:
    lis = list(input('Введите числа для списка:\n'))
    set_s = set(lis)
    print(len(set_s))
    flag_exit = int(input('Нажмите любую клавишу, чтобы выйти или "0" для продолжения'))
