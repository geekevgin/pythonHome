user_input = input('Enter any sentence:')
user_words = user_input.split()
for num, word in enumerate(user_words, 1):
    print(str(num) + '-', str(word[:10]))
