firstName = input('Enter your first name please ? \n')
lastName = input('Enter your last name please ?\n')
fullName = firstName + ' ' + lastName
print(fullName)  
# Input in python will always give you string no matter what even if you enter a number you'll still get a string.
# To change a type from one to another (typecasting) we can use the following syntax.
num = int(2.3); # num will store 2 (It just chops off the decimal thing.)
stringValue = str(2.3)
print(type(num))
print(type(stringValue))
floatValue = float(stringValue);
print(type(floatValue))


