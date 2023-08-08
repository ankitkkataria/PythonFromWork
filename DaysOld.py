age = input('Enter age in years please ? \n')
daysCalculated = float(age) * 365
print(str(age) + " years is " + str(daysCalculated) + " days old")
# Other way of doing the same thing is using the string template literal kind of thing called a formatted string in python
print(f'{age} years is {daysCalculated} days old')