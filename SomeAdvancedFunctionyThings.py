# To accept any number of arguments like min, max functions are able to do you use the * operator it's like ...(rest) operator in JS.
# Here the args(or whatever name you provide) will store all the arguments that are passed in during the function call in a tuple.

def average(*args): # This * operator is the important thing you don't need to use the name args in specific it can be nums or anything but normally people use args.
    total = 0
    for arg in args:
        total += arg
    return total/len(args)      

# Executing the above function with varying number of arguments.
print(average(1,2,3,4,5))
print(average(1,2))

def silly(first,second,*others): # This method requires you to have two arguments minimum and the rest of them will be stored in the others tuple.
    print(f'first arg is : {first}')
    print(f'second arg is : {second}')
    print(f'other args are : {others}')


silly('ajay',1,'ankit',124)

# kwargs (This has a syntax of ** before the name what this does is like *args stored the remaining arguments inside a tuples what this will do is it will just go ahead take all the remaining keyword arguments and put them in a dictionary.)
def printAges(name,age,**kwargs): # You can name kwargs anything.
    print(f'{name} is {age} years old')
    # Rest of the args if passed in will be stored in the kwargs dictionary.
    for k,v in kwargs.items():
        print(f'{k} is {v} years old')

printAges('ankit',25,maxy=34,raxy=23) # Basically kwargs dictionary will look like {'maxy':34, 'raxy': 23}
