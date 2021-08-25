def my_sum_list():
    sum = 0
    while sum != 0:
        str_of_numbers = input('Enter any list of numbers:')
        list_of_numbers = str_of_numbers.split()
    for i in list_of_numbers:
        if i.isdigit():
            sum += int(i)
            return sum
            print(sum)
    else:
        print('You have entered the symbol')
        sum = ''
print(sum)
