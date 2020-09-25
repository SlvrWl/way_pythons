to_exit = 'No'
while to_exit == 'No':
    number_chet = list(input('Введите числа'))
    chet = number_chet[0::2]
    print(chet)
    exi = input('Хотите выйти? "Yes" - да "No" - нет. Ваш ответ? \n ')
    if exi == 'Yes':
        to_exit = 'Yes'
