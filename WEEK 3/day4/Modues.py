# module = a flie containing code you want to include in your program
# use import to include a moudle (built-in or custom)
# useful to break up a large program reusable separate files
# built-in modules = pre-installed with python
# custom modules = created by you or other programmers

# print(help("modules"))  # list all available modules

# import math
# import math as m # aliasing a module
#
# print(m.pi)
#
# from math import pi, e, sqrt  # import specific attributes from a module
# print(pi)
# a,b,c,d,e = 2,3,4,5,6
# print(e ** a)
# print(sqrt(16))
# print(e)
# print(pi * (a ** 2))
# # print(dir(math))  # list all attributes and methods in a module
# print(dir())  # list all attributes and methods in the current namespacef

import example

result = example.pi
result = example.area(5)
result = example.circumference(5)
print(result)