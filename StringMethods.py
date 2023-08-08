name = 'anKiT'
print(name.lower())
print(name.upper())
print(name.capitalize())
# In python docs what the [] means in the args is that that arg is actually optional to put in.
randomString = ",,,,....,.,.,..,..,.,.,..,.,.#####whateverthisistakethisoutplease....#####.,,,"
modifiedString = randomString.strip(",.#") # Doing this will take out all the combinations of .,# symbols from the beginning and end of the string. (If you don't pass in anything it will just remove whitespaces from the beginning and the end of the string these brackets are also called signatures.)h
print(modifiedString)
#lstrip and rstrip also exist they do the same thing but just limited for beginning and trailing characters.
newString = '2kilometers 6kilometers 4kilometers 5kilometers 3kilometers'
newModifiedString = newString.replace("kilometers", "km", 3) # 3rd argument is optional using it you can change only the begining few occurences of that word if you don't put anything there you will remove everything.
print(newModifiedString);
print(newString.find('6k')); # Finds the first occurence of a character.
print(newString.find('meters',4,7)) # Both the args after the first one are optional they give the start and end point index for the string that you have to search for to find the substring and if it doesn't find the substring it will return -1.
print(newString.count('2')) # Similar to find but just returns the count of the substring that is passed in.
print(newString.count('2',1,10))
randomBool = 'a' in 'bat'
print(f'{randomBool} is for "a" in "bat"')
randomBool2 = 2 in [1,4,5,6]
print(randomBool2)
