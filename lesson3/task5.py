def my_list_of_numbers():
    sum = 0
    while sum != '':
        str_of_numbers = input('Enter the list of numbers:')
        list_of_numbers = str_of_numbers.split()
        for i in list_of_numbers:
            try:
                if i == ' ':
                    print(f'sum equals {sum}.')
                    return
                else:
                    sum = sum + int(i)
            except ValueError:
                return ValueError
                print('Enter any number')
        print(f'sum equals {sum}')

