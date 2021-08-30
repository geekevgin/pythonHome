from functools import reduce

num_list = [i for i in range(100, 1001) if (i % 10 == 0)]
multiplication = reduce(lambda a,b: a * b, num_list)
print(multiplication)