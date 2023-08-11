def getTotal(price, qty=1, tax=0.02, discount=0):
    subTotal = price * qty * (1 - discount)
    print(subTotal(1 + tax))


getTotal(9.75, 5, 0.01, 0.5) # It's hard to tell which argument means what when calling the function. So, we use keyword arguments.
getTotal(price=9.75, qty=5, tax=0.01, discount=0.5) # This looks similar to default arguments but that is used while defining the function but this is used while calling it.
getTotal(price=9.75, discount=0.5, qty=5, tax=0.01) # These args can be in any order they don't have to be in the order of the formal arguments.
getTotal(5.50,5,tax=0.025) # If you enter one keyword argument then after that you must only enter keyword arguments like after tax here you can't just put 0.3 you must put discount=0.3 (So, Incase you're using a combination of normal arguments and keyword arguments make sure keyword arguments come at the end.)
# Just one more thing nested functions can access variables defined in their parents as well.
