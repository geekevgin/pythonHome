def my_data_info(name, surname, year_of_birth, city_of_residence, email, phone_number):
    result = f'{surname} {name}, {year_of_birth}, living in {city_of_residence}. Contact information {phone_number} and {email}'
    return result
print(my_data_info('Rob', 'Pat', 1987, 'Rome', 87654291, 'ent@it'))