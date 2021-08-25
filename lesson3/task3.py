def my_func_sum_1(num_1, num_2, num_3):
    res_my_func_sum_1 = [num_1, num_2, num_3]
    res_my_func_sum_1.remove(min(num_1, num_2, num_3))
    return sum(res_my_func_sum_1)
print(my_func_sum_1(5, 4, 6))