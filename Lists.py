# List in python is basically a array that can store multiple types of elements as well.
randomNums = [1, 4, 5, 23, 6, 2]

randomList = list(
    "Hello"
)  # This works like the ... spread opertor in JS any iteratable that you pass into the list it will take each of the components and return it to you in a list/arr.
randomList2 = list(range(2, 24))

print(randomList)
print(randomList2)

len(
    randomList2
)  # This here too will return the length of the array to you obviously while iterating you would want to got till one index less.
randomNums.append(42)  # append is basically push_back method.
print(randomNums)
randomNums.extend(
    [3, 43, 54, 2]
)  # extend method takes the list and takes each of it's elements and pushs into the randomNums list.
print(randomNums)
# If you do randomNums.append([3,23,43,56,6]) your array/list will look like [1, 4, 5, 23, 6, 2, 42, 3, 43, 54, 2,[3,23,43,56,6]]
randomNums.append([3, 23, 43, 56, 6])
randomNums.insert(
    0, 2132
)  # This will insert 2132 at the index 0 in the randomNums array.
randomNums.insert(
    len(randomNums), 12331
)  # Instead of using append you can also use this but idk why you would do that ?
print(randomNums)
# list.insert(indexWhereYouWantToInsert,whatYouWantToInsert)
randomNumsSpliced = randomNums[1:4]
randomNumsSpliced2 = randomNums[:5]  
randomNumsSpliced3 = randomNums[5:]
randomNumsSpliced4 = randomNums[
    1:8:2
]  # All the splice here work exactly like the one used in strings
randomNumsSpliced5 = randomNums[
    ::3
]  # This will give me all the elements in third place from beginning to end of the list.
print(randomNumsSpliced)
print(randomNumsSpliced2)
print(randomNumsSpliced3)
print(randomNumsSpliced4)
# You can also use a splice syntax to update the list altogether which is something that you can't really do in strings.
nums = [1, 2, 4, 5, 6]
print(nums)
nums[0:3] = ["a", "b", "c"]
print(nums)
nums2 = [1, 2, 4, 5, 6]
nums2[0:3] = ["a", "b", "c", "d"]
print(nums2)
nums3 = [1, 2, 4, 5, 6]
nums3[0:3] = ["a"]
print(nums3)

# Removing Elements
numbers = [1, 42, 5, 6, 7, 2]
print(numbers)
numbers.clear()  # If you want to delete all the elements.
print(numbers)

numbers = [1, 42, 5, 6, 7, 2, 42]
print(numbers)
numbers.remove(
    42
)  # This is basically findOneAndDelete that's it. It deletes the first occurence of the element but remember this doesn't return this deleted element.
print(numbers)

numbers2 = [1, 24, 23, 12, 1214, 2323]
print(numbers2)
lastElement = (
    numbers2.pop()
)  # If you don't pass in any arg it just pops back the last element and also returns it.
print(lastElement)
print(numbers2)

numbers3 = [1, 24, 23, 12, 1214, 2323]
print(numbers3)
elementAtFirstIndex = numbers3.pop(
    1
)  # Now it will go ahead and pop that element at first index and return it as well.
print(elementAtFirstIndex)
print(numbers3)

# You can also delete elements using the del statement.
numbers3 = [1, 24, 23, 12, 1214, 2323]
print(numbers3)

del numbers3[
    2
]  # This will delete the number at index 2 in this array but won't return it.
print(numbers3)

del numbers3[
    ::2
]  # This will delete every second element from your list. (You can use this method to delete slices that's the only place using this makes a little bit of sense.)
print(numbers3)

# Iterating over the lists
names = ["ankit", "aman", "ashish"]

for name in names:
    print(f"I'm mailing {name}")


def average(
    nums,
):  # Defining a function that returns the average of all the numbers in an array.
    total = 0
    for num in nums:
        total += num
    return total / len(nums)


numbers = [1, 4, 5, 6, 7, 7, 8]
avg = average(numbers)
print(avg)
print(min(numbers))
print(min(1, 3))
