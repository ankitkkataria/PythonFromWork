age = input("How old are you ?\n")
age = int(age)

if age >= 21:
    print('===========')
    print("Come on in!")
    print('===========')
else:
    print("Go home kid!")


num = 12

if num > 1:
    print('Yoo yoo')
elif num < 1:
    print('Do')
else:
    print("Poo poo")

# There is a function that's called round(floatValue,numOfDigitsYouWouldLikeItToBeRounded)
# So, round(20.23452,3) = 20.234