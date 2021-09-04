the_list_of_rating = [1, 2, 4, 6, 7, 8]
user_rating_num = input('Enter any number of rating:')

for index, elem in enumerate(user_rating_num):
    if user_rating_num > elem:
        the_list_of_rating.insert(index, elem)

print(the_list_of_rating)
