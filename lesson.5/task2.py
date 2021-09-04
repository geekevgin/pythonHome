my_file = open('text_task1.txt', 'r')
content = my_file.read()
print(f'File contents:\n: {content}')
content = my_file.readlines()
print(f'number of strings :\n - {len(content)}')
for i in range(len(content)):
    print(f'number of symbols {i + 1} in string {len(content[i])}')

my_file.close()