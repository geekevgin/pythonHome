num_list = [100, 101, 23, 14, 98, 7, 9, 67]
res_list = [num_list[i] for i in range(len(num_list)) if num_list[i] > num_list[i - 1] and i > 0]
print(res_list)
