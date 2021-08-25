def my_func_sum(num_1, num_2, num_3):
    res_my_func_sum = [num_1, num_2, num_3]
    res_my_func_sum.remove(min(num_1, num_2, num_3))
    return sum(res_my_func_sum)
print(my_func_sum(5, 4, 6))