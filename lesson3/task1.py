def my_division(num_1, num_2):
    try:
        return int(num_1) / int(num_2)
    except ZeroDivisionError:
        return 'NO Zero Division'
num_1 = int(input('Enter the first number:'))
num_2 = int(input('Enter the second number:'))
print(my_division(num_1, num_2))

def my_division_1(num_1, num_2):
    if num_2 > 0:
        num_3 = num_1 / num_2
    else:
        print('ZeroDivisionError')
    return num_3
num_1 = int(input('Enter the first number:'))
num_2 = int(input('Enter the second number:'))
print(my_division_1(num_1, num_2))