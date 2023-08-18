# Tuples can contain list as elements so just because tuples are immutable that doesn't mean it's elements have to be immutable as well.
# But in sets all the elements must be immutable as well.
# Sets are unordered collections with no duplicate elements.
# In Sets we can :-
# • Add and delete elements.
# • Iterate over elements.
# • Check to see if element is in a set.
# • Use set operators: union, intersection, etc.

# Creating an set
evens = {2, 4, 6, 8}
randomSet = {2,True,"random string"} # You can only put immutable elements in a set so you can't put lists and dictionaries only cause of the same rule as the hashmap keys these elements in set also have to be hashable.

# Creating an empty set so you can add elements to it later.
# emptySet = {} # This is a wrong way of making a empty set actually just simply using empty curly braces makes us an empty dictionary.
emptySet = set() # This way you'll be able to make it no issues.

# To make a set with only one value that's very simple.
singleElementSet = {1}

# If you make a set with duplicate values it will automatically remove those duplicates.
randomSet2 = {2,2,2,2,4,5,6,7}
print(randomSet2)

randomSet3 = {1,24,5}
print(randomSet3)
randomSet3.add(-5) # This is used to add elements to the set. 
print(randomSet3) # Sets are not sorted.

randomSet3.remove(-5) # This method is used to remove elements from a set. (But it throws an error if the element doesn't exist so for those cases you can use the discard method.)
randomSet3.discard(132) # This will not be throwing an error.

print(randomSet3) 

# To find out the length of a set the len function still works.
print(len(randomSet3))

# You can't access the elements of a set using the array subscript operator.
# randomSet3[0] # This will give you an error.

# To delete all the elements of a set.
randomSet.clear() # This method again deletes all the elements of  a set.
print(randomSet) # This will print set() and not {} cause that means an empty hashmap/dictionary.

# Again since set is mutable that means all the == and is will work here.
# So, to compare if all the elements are same of not you can use == and in case if you want to compare if the same set is being pointed by 2 variables then you can just use the is operator.

# in operator also works in sets.
print(2 in evens) # Will print True.

# You can also iterate over sets.
for setElement in randomSet3:
    print(setElement)

# Union among two sets.
set1 = {1,2,3}
set2 = {2,3,4}

set3 = set1 | set2 # Other way is set1.union(set2) 
print(set3)

# Intersection among two sets.
set4 = set1 & set2 
print(set4)

# Difference among two sets.
set5 = set1 - set2 # Here the order actually matters set1 - set2 might be differant than set2 - set1.
print(set5)

# Why Use sets?
# • Sets make it very easy/ fast to check if a value exists in a collection.
# • Sets are an easy way to remove duplicates from a collection.

# Use cases of sets :-
# Let's say you have zipcodes okay and you have to check if this input that you got exists in those zipcodes it's better to store them in a set cause values in the set are hashed otherwise if you store them in a list/array a linear search will be conducted.
# Second is if you have a list and you want to remove duplicates you can convert it into an set and than later if you want you can convert it back to a list that way we will get a list containing only unique values.
list3 = [2,3,3,3,3]
randomSet4 = set(list3)
print(randomSet4)
list3Unique = list(randomSet4)
print(list3Unique)

# Shorter way is 
list3Uniquee = list(set(list3))
print(list3Uniquee)
