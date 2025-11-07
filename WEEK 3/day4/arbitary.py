# *args = allows you to pass multiple non-key arguments
#**kwargs = allows you to pass multiple keyword arguments
# * unpacking operator

# def add(a,b):
    # return a + b

# print(add(1,2,3)) # this will cause an error because add only takes 2 arguments

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1,3,2))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("dr.","Spongebob","Squarepants")

# def print_address(**kwargs):
#     # print(type(kwargs))
#     # pass
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
#
# print_address(street="123 Fake St." ,
#               city="detroit",
#               state="MI",
#               zip="54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()

    if "apt" in  kwargs:
        print(f"{kwargs.get('street')} Apt {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
        print(f"{kwargs.get('street')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.","Spongebob","Squarepants","III",
               street="123 Fake St.",
               # apt="100",
               pobox="PO BOX #1001",
               city="Detroit",
               state="MI",
               zip="54321")

