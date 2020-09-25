def percent (per_args):
    ''' Нахождение процента '''
    split_args = per_args.split('%')
    result = int(split_args[0]) / 100
    return result

def plus_minus_ar (p_m_args):
    ''' Сложение и вычитание выражения '''
    if p_m_args.find('+') != -1:
        split_args = p_m_args.split('+')
        result = int(split_args[0]) + int(split_args[1])
    else:
        split_args = p_m_args.split('-')
        result = int(split_args[0]) - int(split_args[1])
    return result

def quadro_degre (qd_args):
    '''Функция возведения в квадрат или степень'''
    splited_qd = qd_args.split('**')
    if splited_qd[-1] == '':
        result =  int(splited_qd[0]) ** 2
    else:
        result = int(splited_qd[0]) ** int(splited_qd[1])
    return result

def multiply_split (m_s_args):
    '''Функция умножения или деления'''
    if m_s_args.find('/') != -1:
        splited_m_s = m_s_args.split('/')
        result = int(splited_m_s[0]) / int(splited_m_s[1])
    else:
        splited_m_s = m_s_args.split('*')
        result = int(splited_m_s[0]) * int(splited_m_s[1])
    return result
flag = 0
while flag == 0:
    input_arg = str(input('Введите выражение для подсчёта'))
    if input_arg.find('+') != -1 or input_arg.find('-') != -1:
        print(plus_minus_ar(input_arg))
    elif input_arg.find('%') != -1:
        print(percent(input_arg))
    elif input_arg.find('**') != -1:
        print(quadro_degre(input_arg))
    elif input_arg.find('*') != -1 or input_arg.find('/') != -1:
        print(multiply_split(input_arg.find('*')))
    else:
        print('Я не понимаю, что вы ввели')
    flag = int(input('Для выхода нажмите любую клавишу. Для продолжения введите "0"'))
