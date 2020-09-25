flag_to_exit = 0
while flag_to_exit == 0:
    in_out = input('Введите значение ключа\n')
    di = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
    for i in di:
        if str(di.get(i)) == in_out:
            print('Значение совпадает с ключом ', i)
    flag_to_exit = int(input('Если хотите продолжить введите 0.\nЕсли хотите выйти нажмите любую клавишу'))
