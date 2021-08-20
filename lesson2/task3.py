num_of_month = (input('Enter any number of month: '))
w = 'winter'
sp = 'spring'
s = 'summer'
a = 'fall'

month_of_year_dict = {'1': w, '2': w, '3': sp, '4': sp, '5': sp, '6': s, '7': s, '8': s, '9': a, '10': a, '11': a, '12': w}
print(month_of_year_dict[num_of_month])

month_of_year_list = [w, w, sp, sp, sp, s, s, s, a, a, a, w ]
print(month_of_year_list[int(num_of_month) - 1])