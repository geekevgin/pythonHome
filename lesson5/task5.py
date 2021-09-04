with open('text_task5.txt', 'w') as file:
    numbers = input('Enter numbers:\n')
    file.writelines(numbers)
    num = numbers.split()
    print(sum(map(int, num)))