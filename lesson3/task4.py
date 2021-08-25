def my_func_pow(x, y):
    res_my_func_pow = x ** (y)
    return x ** (y)

print(my_func_pow(10, -3))

def my_func_pow_1(x, y):
    a = 1
    for i in range(abs(y)):
        a = a * x
    return 1/a
print(my_func_pow_1(2, - 4))
