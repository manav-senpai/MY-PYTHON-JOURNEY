# variable scope = where a vairable is visible and accessible
# global scope = visible to the entire file
# local scope = visible only inside the function
# enclosing scope = visible to nested functions
# built-in scope = names preassigned in the built-in names module
# scope resulution = LEGB rule (local, enclosing, global, built-in)
x = 3
def func1():
    print(x)
def func2():
    print(x)

func2()

func1()
