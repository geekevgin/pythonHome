# subjects = {}
# with open('text_task6.txt') as file:
#     file_lines = file.readlines()
#     for line in file_lines:
#         subjects, lecture, practise, lab = line.split()
#         subjects[subjects] = int(lecture) + int(practise) + int(lab)
#         print(f'Average hour\n {subjects}')
#

subjects = {}
with open('text_task6.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        subj_info = line.split
        hour = 0
        for elem in subj_info[1:]:
            if elem != '-':
                num = 0
                for i in elem:
                    if i.isdigit():
                        num = num + i
                        hour = hour = int(num)
        subjects.update({subj_info[0]:hour})
print(subjects)
