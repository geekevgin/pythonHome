rus_num = {
    'One': 'один',
    'Two': 'два',
    'Three': 'три',
    'Four':'четыре'
}
rus_file = []
with open ('text_task4.txt') as file:
    file_line = file.readlines()
    for line in file:
        line = line.split()
        rus_num = rus_num.get(line[0])
with open('new_text_task4.txt', 'w') as file_2:
    file_2.writelines(rus_file)


