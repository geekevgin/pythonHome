with open('text_task1.txt', 'w') as file:
    words_input = input('Enter some text:\n')
    while words_input:
        file.writelines(f'{words_input}\n')
        words_input = input('Enter some text:\n')
        if not words_input:
            break

