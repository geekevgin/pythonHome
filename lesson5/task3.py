with open('text_task3.txt') as file:
    file_lines = file.readlines()
    workers = {}
    total_salary = 0
for line in file_lines:
    database_of_workers = line.split()
    workers.update({database_of_workers[0]: float(database_of_workers[1])})
    total_salary = total_salary + float(database_of_workers[1])
average_salary = total_salary / len(workers)
print(average_salary)
for w, s in workers.items():
    if s < 20000:
        print(f'{w}:{s}')