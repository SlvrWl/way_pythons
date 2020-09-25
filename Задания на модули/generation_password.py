from random import *
'''Хей, эта мини-программа записывает в файл данные в виде
   названия сайта, логина, почты и пароля в файл, а ещё
   она генерирует пароль:) '''
flag = 0
while flag == 0:
    def gen_psw():
        passwd = []
        while len(passwd) != 12:
            passwd.append(choice('!@#$%^&*()-+'))
            passwd.append(choice('1234567890'))
            passwd.append(choice('abcdefghijklmnopqrstuvwxyz'))
            passwd.append(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
            shuffle(passwd)
            str_pswd = ''
            str_pswd = str_pswd.join(passwd)
        return str_pswd


    site = str(input('Чувак, введи название сайта\nдля которого хочешь сохранить данные для входа:\n')) + ','
    login = str(input('Хорош! А теперь введи логин от сайта:\n')) + ','
    email = str(input('Чувак, введи свой майл, чтобы не потерять акк:\n')) + ','

    str_pswd = gen_psw()
    with open('C:\\Users\mrvli\\Desktop\\psqwe.txt', 'r+') as pswd:
        string_log_in = []
        if 'EMAIL' not in pswd:
            title = ['SITE,', 'LOGIN,', 'EMAIL,', 'PASSWORD']
            title_string = ''
            title_string = title_string.join(title)
            string_log_in.append(title_string)

        log_in = []
        log_in.append(site)
        log_in.append(login)
        log_in.append(email)
        log_in.append(str_pswd)
        mass_data = ''
        mass_data = mass_data.join(log_in)
        string_log_in.append(mass_data)
        print(string_log_in)
        [pswd.write(line + '\n') for line in string_log_in]

    print('Чувак, я создал для тебя пароль и сохранил все данные для входа в файл:\n',gen_psw())
    flag = int(input('Продолжим заполнять файл паролями? 0 - "Да" Любая клавиша - "Нет":\n'))
