num_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_num_list = [i for i in num_list if num_list.count(i) == 1]
print(res_num_list)