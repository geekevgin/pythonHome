user_input = input('Enter a list:')
input_user_list = user_input.split()

len_list = len(input_user_list)
i = 0

while i < len_list - 1:
    input_user_list[i], input_user_list[i + 1] = input_user_list[i+1], input_user_list[i]
    i += 2
print(input_user_list)

