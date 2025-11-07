# default arguments = a default value for certain parameters
# defalult is used when that argument is omitted
#make your functions more flexible, reduces number of arguments
# 1. postitional 2. default 3. keyword 4. variable length

# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount ) * ( 1 + tax )
#
# print(net_price(500,0,0.05 ))

# def net_price(list_price, discount=5, tax=0.07):
#     return list_price * (1 - discount ) * ( 1 + tax )
# #
# # print(net_price(500,0 ))
# print(net_price(534))

import time

def count(end,start=0):
    for x in range(start,end):
        print(x)
        time.sleep(1)
    print("Done!")

count(50,12)