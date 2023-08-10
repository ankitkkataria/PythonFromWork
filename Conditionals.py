age = input("How old are you ?\n")
age = int(age)

if age >= 21:
    print("===========")
    print("Come on in!")
    print("===========")
else:
    print("Go home kid!")


num = 12

if num > 1:
    print("Yoo yoo")
elif num < 1:
    print("Do")
else:
    print("Poo poo")

# There is a function that's called round(floatValue,numOfDigitsYouWouldLikeItToBeRounded)
# So, round(20.23452,3) = 20.234

x = 16

if x == 23:
    print("Yes")
elif x < 23:
    if x < 15:
        print("It is lesser than 15")
    else:
        print("It is greater than 15 but lesser than 23")
else:
    print("It is greater than 23")

y = 12

if y > 1 and y < 13:
    print("It is greater than 1 and lower than 13")

xtra = 12

if not xtra == 12:
    print("Not equal to 12")
else:
    print("Equal to 12 my boi")


randomNum = -1
if randomNum:  # So, You can understand just 0 or 0.0 as a number has a false value.
    print("I'm printing even though the value in the condition is negative.")

answer = input("Please say (hi) here :)\n")
print(f"You just entered {answer}")

while answer != "hi":
    answer = input("Please say (hi) here :)\n")
    print(f"You just entered {answer}")

print("Hi! Bro thanks for saying hi mate")


moni = 12

if moni > 12:
    if moni < 15:
        print("you are still not that rich")
    else:
        print("you are rich bro")
else:
    print("You are basicaly homeless")


