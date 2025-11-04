#nested loop = A loop within another loop ( outer, inner )
#               OUTER LOOP :
#                        INNER LOOP :

row = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))
symbol = input("Enter the symbol to use : ")


for x in range(row):
    for y in range(columns):
        print(symbol, end= " ")
    print()