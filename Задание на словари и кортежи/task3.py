list_string = str(input('Введите список строк через запятую\n'))
l_s = list_string.split(',')
print(l_s)
len_list = len(l_s)
print(len_list)
key = []
value = []
dict_list = {'a', 'b', 'c'}
for i in range(0, len_list - 1):
    for j in range(i + 1, len_list - 1):
        if l_s[i] == l_s[j]:
            key.append(l_s[i])
print(key)
