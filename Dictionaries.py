# Dictionaries are like object literals in JS.
# Here keys should only be immutable types like strings, numbers, booleans or tuples.
# You can't make a list/array as a key python will go and throw error if you try to do that.
# Also value can be literally anything like string,number,list,function anything.

randomDict = {"name": "Ankit", "age": 25}  # This is a valid dictionary

# One thing that I thought was an interesting thing colt mentioned was like arrays can also be thought of as key-value pairs it's just keys are numbers starting at 0's.
# In a similar fashion in a dictionary it's just that the keys can be any immutable type.

print(randomDict["name"])

# print(randomDict['address']) # Since this key doesn't exist in the dictionary this will give you an error.

randomDict2 = {True: 23, 45: "Hi"}
print(randomDict2[True])
print(randomDict2[45])

randomDict["age"] = 26  # This will update the existing key's value.
randomDict[
    "address"
] = "jind"  # This will see oh! address as a key doesn't even exist so it will make that key and add the value jind to it. (Also one dictionary can only have unique keys.)

fruitPrices = {
    "mango": 40,
    "guava": 20,
    "banana": 40,
}

product = input(
    "Enter the fruit name you would like to get to know the price of ?"
).lower()

# If you just go and access fruitPrices[product] and the product doesn't exist it will give an error so we can do this.

if product in fruitPrices:
    price = fruitPrices[product]
    print(f"{product} price is Rs.{price}")
else:
    print("We do not have information about this product. Sorry :(")

# Other way of doing it is using the .get() method in dictionary which returns None if it doesn't find a key rather than throwing an error.

product = input(
    "Enter the fruit name you would like to get to know the price of ?"
).lower()
price = fruitPrices.get(product)

if price: 
    print(f"{product} price is Rs.{price}")
else:
    print("We do not have information about this product. Sorry :(")

# Deleting enteries from dictionary

# pop() method
priceOfMango = fruitPrices.pop('mango') # This will pop the key-value pair of mango. (But it will also return the value of mango.)
print(priceOfMango)

# popitem() method
fruitPrices['chiku'] = 12
randomTuple = fruitPrices.popitem() # This method just returns the tuple of (key,value) of the pair that was last added in the dictionary.
print(randomTuple)

# del statement
del fruitPrices['banana'] # This will delete the key-value pair of chiku without returning it.
print(fruitPrices)

# clear() method
fruitPrices.clear() # This will clear the entire dictionary all together
print(fruitPrices)

# dictionaries are mutable too just like arrays/lists you have the same things about shallow copy and comparing using == and is operators.
# If you go and assign them to each other only a reference will be added so if you want to copy you'll have to use .copy() method.
# If you want to do deep copy you will have to use the copy.deepcopy() method.

testScores = {
    'Ankit' : 99,
    'Aman' : 83,
    'Ashish' : 90,
    'Ajay' : 95,
    'Abhay' : 93,
}

# testScores.keys() returns the dict_values data structure (where it will contain all the key values of this dictionary) it's not exactly a list but it's iteratable if you want to convert it to a list then you can just do list(testScores.keys())

for student in testScores.keys(): # To iterate over the keys.
    print(student)

for score in testScores.values(): # To iterate over the values.
    print(score)

for student in testScores.keys(): # You can access values if you have the key.
    print(student,testScores[student])

for entry in testScores.items(): # If you want the entire entry your testScores.items() it will return the list of tuples of your dictionary.
    print(entry)    

for k,v in testScores.items(): # You can even destructure each of tuple here itself. (tuple is just a pair in c++)
    print(k,v)

bestStudent = ''
maxScore = 0
for student,score in testScores.items():
    if score > maxScore:
        maxScore = score
        bestStudent = student
print(f'The best perfoming student is {bestStudent} and he/she has {maxScore} marks')        
