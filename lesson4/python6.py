
from itertools import cycle, count
list_1 = [1, 2, 3, 4, 5]

count = 1
for i in cycle(list_1):
    if count > 5:
        break
    print(list_1)
    count += 2

for i in list_1:
    if i == 3:
        break
    print(list_1)