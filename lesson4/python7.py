def my_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * 1
        yield factorial
num = 6
factorial = my_factorial(num)
print(factorial)