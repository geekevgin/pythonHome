num = int(input('enter a number:'))
max_num = 0
while num > 0:
    b = num % 10
    if max_num < b:
        max_num = b
    num = num // 10
print(max_num)
