def my_func_sum_1(num_1, num_2, num_3):
    res_my_func_sum_1 = [num_1, num_2, num_3]
    res_my_func_sum_1.remove(min(num_1, num_2, num_3))
    return sum(res_my_func_sum_1)
print(my_func_sum_1(5, 4, 6))

def my_func(x, y, z):
    if x > y or x > z and y > z:
        print(x + y)
        return x + y
    elif y > x or y > z and x > z:
        print(y + z)
        return y + z
    else:
        print(y + z)
        return y + z
print(my_func(5, 2, 3))
