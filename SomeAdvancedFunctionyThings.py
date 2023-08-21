# To accept any number of arguments like min, max functions are able to do you use the * operator it's like ...(rest) operator in JS.
# Here the args(or whatever name you provide) will store all the arguments that are passed in during the function call in a tuple.


def average(
    *args,
):  # This * operator is the important thing you don't need to use the name args in specific it can be nums or anything but normally people use args.
    total = 0
    for arg in args:
        total += arg
    return total / len(args)


# Executing the above function with varying number of arguments.
print(average(1, 2, 3, 4, 5))
print(average(1, 2))


def silly(
    first, second, *others
):  # This method requires you to have two arguments minimum and the rest of them will be stored in the others tuple.
    print(f"first arg is : {first}")
    print(f"second arg is : {second}")
    print(f"other args are : {others}")


silly("ajay", 1, "ankit", 124)


# kwargs (This has a syntax of ** before the name what this does is like *args stored the remaining arguments inside a tuples what this will do is it will just go ahead take all the remaining keyword arguments and put them in a dictionary.)
def printAges(name, age, **kwargs):  # You can name kwargs anything.
    print(f"{name} is {age} years old")
    # Rest of the args if passed in will be stored in the kwargs dictionary.
    for k, v in kwargs.items():
        print(f"{k} is {v} years old")


printAges(
    "ankit", 25, maxy=34, raxy=23
)  # Basically kwargs dictionary will look like {'maxy':34, 'raxy': 23}

# If your function has all the types of arguments like normal parameters, default parameters, *args or **kwargs.
# We all the that default parameters should come after normal parameters.
# But if everything is there you should use only this ordre down below.
# (1.normal parameters, 2.*args, 3.default parameters, 4.**kwargs) # If you want explanation for this watch colt's video on this topic.

# A weird gotcha with default parameters.
# If you have a mutable object like a list as an default argument that can cause weird issues.
# For example :-


def addToListThrice(
    val, lst=[]
):  # A function that adds the val thrice to the list passed in otherwise it just takes an empty list and adds val thrice and returns the list. (I have put in a empty list in default args just for example but it can even be a filled up list or an empty dictionary or filled up dictionary they are all mutable data structures.)
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst


print(addToListThrice(1, [1, 2, 3]))  # This works normally.
print(addToListThrice(2))  # This also works normally.
print(
    addToListThrice(1)
)  # This causes issue val is added to the previous default list rather than being added to a new list. (This is cause default arguments are shared or are common to all the function calls so when you call it again it python says oh! i have a default list i'll just add to that.)

# So if you want to get a new list if you're not passing in a list everytime this is the method.


def addToListThriceFinal(val, lst=None):
    if lst is None:  # You can also use == in place of is.
        lst = []
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst


print(addToListThriceFinal(1, [1, 2, 3]))
print(addToListThriceFinal(2))
print(addToListThriceFinal(1))

# Just like spread(...) in JS we have a spread/unpacking operator here too that is *.
# Like you had an function called average above that is expecting any number of args and it will give you the average.
# But it only works when you call it like average(1,2,3,4,4,5)
# But if you have a list like nums = [1,2,3,4,5,6,7,8,9,10]
# And you do average(nums) it will give you an error cause it's exepecting any number of individual arguments it is not expecting a list.
# So, while calling the function itself you can destructure the list.
nums = [1,2,3,4,5,6,7,8,9,10]
print(average(*nums)) # So, This will work.

nums2 = [1,2,3,nums] # This will make nums2 = [1,2,3,[1,2,3,4,5,6,7,8,9,10]]
print(nums2)

nums2 = [1,2,3,*nums]# This will make nums2 = [1,2,3,1,2,3,4,5,6,7,8,9,10]
print(nums2)