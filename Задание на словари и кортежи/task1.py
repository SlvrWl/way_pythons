d = dict(a = 1, b = 2)
k = 'b'
def get_values(d, k):
    val = d[k]
    print('Значение вашего ключа:', val)
print(get_values(d, k))
