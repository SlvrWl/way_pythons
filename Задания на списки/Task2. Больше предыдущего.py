#Программа находит в списке число, которое больше предыдудещго и заносит его в отдельный список
flag = 0
while flag == 0:
    number = list(input('Введите числа и я выведу Вам все числа,\nкоторые больше предыдущего\n'))
    number_plus = []
    len_list = len(number)
    for i in range(0, len_list - 1):
        if number[i + 1] > number[i]:
            number_plus.append(number[i + 1])
    print(number_plus)
    to_exit = int(input('Для продолжения введите "0", а для выхода любое число '))
    print('Вот список чисел, которые больше предыдущего числа в вашем списке')
    flag = to_exit
