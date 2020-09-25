#Простенький поиск наибольшего числа в массиве/simple find max number in array
S = list(input('Введите массив чисел'))
max = S[0]
for i in range(len(S)):
    if i < len(S):
        if S[i] > max:
            max = S[i]
print('Максимальное число: ', max)
