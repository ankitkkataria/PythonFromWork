# To concatenate two lists/arrays we can use the plus symbol.
odds = [1, 3, 5]
evens = [2, 4, 6]
both = odds + evens
print(odds)
print(evens)
print(both)

# To duplicate a list use multiply symbol.
randomList = [1, 3, 5] * 20
print(randomList)

# in operator
randomBoolean = 1 in odds  # This will return true.
randomBoolean2 = 1 not in odds  # This will return false.

# count method
randomList = [1, 24, 5, 6, 7, 8, 7, 9]
print(randomList.count(7))

# sort method
randomList = [1, 24, 5, 6, 7, 8, 7, 9]
randomList.sort()  # sorts the list in place (meaning actual list will be modified)
print(randomList)

# sort method with reverse option
randomList = [
    1,
    2,
    53,
    5,
    6,
    7,
    8,
    89,
]
randomList.sort(reverse=True)
print(randomList)

# reverse method
randomList.reverse()
print(randomList)

# Variables and lists are assigned differently.
age = 5
num = age # Both of these variables have their own copy of 5.
age -= 1
print("age", age)
print("num", num)

list1 = [1, 2, 3]
list2 = list1 # Both of these lists refer to the same memory (So, just remember assigning lists to each other new variable makes the new variable point to the current list that's it)
list2.append(4)
print("list1", list1)
print("list2", list2)

# This is completely differant from the above case.
list3 = [1, 2, 3]
list4 = [1, 2, 3] 
list4.append(4)
print("list3", list3) 
print("list4", list4)

# == vs is operator (Basically == is used to compare the elements of two lists to see if they are equal of not and (is) operator's purpose is to compare of two lists are the having the same location in memory)
list5 = [1,3,4]
list6 = [1,3,4]

print('list5 == list6',list5 == list6) # Also the order of elements should also be same they can't be in any order as long as the elements are same.
print('list5 is list6',list5 is list6) 

print('list1 == list2', list1 == list2)
print('list1 is list6',list1 is list6) 

# split() method on string
randomString = '03/01/32'
listy = randomString.split('/')
print(listy) # The string will be broken by that character and will be sent to the list.

# join() method on string
randomList = ['Ankit','Kumar','Kataria']
stringy = '-'.join(randomList)
print(stringy)

# Destructuring in python is called unpacking
randomList = ['Ankit','Kumar','Kataria']
firstName,middleName,lastName = randomList
print(firstName,middleName,lastName)

randomList2 = ['Ankit','Aman','Ashish','Ajay','Rajesh']
gold,silver,bronze,*others = randomList2 # Here * works like ... or rest operator in JS. It just goes ahead and captures the remaining.
print(gold,silver,bronze,others)

randomList3 = [1,2,3,4,5,6,7,8]
num1,num2,*others,num7,num8 = randomList3
print(num1,num2,others,num7,num8)

# To spread a list in python just use the * operator.
randomList = [1,2,3,4,5,6]
randomList2 = [10,*randomList] # This can also be done using the extend functionality 
print(randomList)
print(randomList2)

# copy operator to actually copy the list to other list and not just reference it. (this only does a shallow copy meaning the nested lists are still going to be referenced and the changes in the nested lists will be reflected in both the lists)
list1 = [1,2,3] 
# list2 = list1 (This won't work cause it will just make list2 to point to list1)
list2 = list1.copy() 
a = list1 == list2
b = list1 is list2 
print(a)
print(b)

# One other way of doing shallow copy is using the slice operator
list1 = [1,2,3]
list2 = list1[:]

# But if you want to do deep copy you can do it this way
import copy # First import copy library
list1 = [1,2,3,[4,5],6]
list2 = copy.deepcopy(list1)
a = list1 == list2
b = list1 is list2 
print(a)
print(b)

