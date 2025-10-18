# indexing = accessing elements of sequence using [] (indexing operator ) [start : end : step ]
from traceback import print_tb

credit_number = "1234-2342-1234-6456-7653"

# print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::2])

#create a program to get last 4 digits of the number

credit_number_rev = credit_number[::-1]
last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")
print(credit_number_rev)