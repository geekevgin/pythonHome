def my_list_of_numbers():
    sum = 0
    while sum != '':
        str_of_numbers = input('Enter any list of numbers:')
        list_of_numbers = str_of_numbers.split()
        for i in list_of_numbers:
            if i.isdigit():
                sum = sum + int(i)
                return sum
        else:
            print('You have entered the symbol')

print(my_list_of_numbers())
