
# Issue - 1 --------------------------
# import csv 

# file = open('Data/portfolio.csv')

# rows = csv.reader(file)

# def subroutine():
#     print (next(rows))
#     if next(rows) != []:
#        subroutine()
#     else:
#         print("The End")
    

# subroutine()
#Issue -1 ---------------------------

record = {}
with open('Data/prices.csv', 'rt') as file: 
    count = 0
    for line in file:
        count += 1 
    
    while count > 0: 
        row = line.split(',')
        record[row[0]] = float(row[1])
        print(row)

        count -= 1 



    
#     line = 0
#     while line < 
#     for line in file:
    
#         row = line.split(',')
#         record[row[0]] = float(row[1])

# print(record)


