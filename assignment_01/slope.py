import math
# This program sums a series of numbers entered by the user.
def findsum ():
    n = int(input ("How many numbers are you summing?"))
    numbers = eval(input ("What numbers would you like to sum?"))
    total = 0
    for i in numbers:
        total += i
        print("The sum of the series is:", total)
findsum ()