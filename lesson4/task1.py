import sys
from sys import argv
production = float(sys.argv[1])
rate = float(sys.argv[2])
bonus = float(sys.argv[3])
salary = production * rate + bonus
print(salary)