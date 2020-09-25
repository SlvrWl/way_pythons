var_1 = [1,2,3]
var_2 = [0,1,4]
def func(a):
    var_1 = []
    for i in a:
        var_1.append(i**2)
    return var_1

print(func(var_2))
print(var_1)
