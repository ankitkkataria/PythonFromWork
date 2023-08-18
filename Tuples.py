# Tuples are just immutable (meaning you can't change anything in them) lists.
# Tuples are ordered and indexed.

t = ("ankit", "aman", "ajay", "vijay")  # This is a tuple
t2 = ("ankit", 23, ["ad", "asd"], True)  # This is a tuple

# If you want to make a tuple having a single element
t3 = "ankit"  # Won't work cause python doesn't know what you're trying to do it thinks you're trying to do something like t3 = (4*5) * 2

# So, rather do this
t3 = ("ankit",)
# or
t3 = ("ankit",)

# You can't push or pop anything in tuple nor can you change the values of any of the elements in a tuple that's something that you should take note of.

print(t[2])  # Accessing a tuple is easy just like arrays you can access these as well.
sliceOft = t[1:2]  # You can slice as well.

# There are only two methods for tuples.

# 1) index()
t.index("ajay")  # Will return 2.

# 2) count()
t.index("ankit")  # Will return 1.

# Tuples can also be used to iterate over using for loops.
for name in t:
    print(name)

# In operator also works with tuples.
randomBool = "ankit" in t
print(randomBool)

# Why use tuples?
# They are more efficient than lists
# Use them for data that shouldn't change
# Some methods return them like dict.items()
# They can be used as keys in a dictionary cause unlike lists these are immutable so if you want to do something like (lang,lat): 'Jind,Haryana' in a dictionary you can but you can't do [lang,lat] that's it.

# Tuples can contain list as elements so just because tuples are immutable that doesn't mean it's elements have to be immutable as well.
# But in sets all the elements must be immutable as well.


