
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

# record = {}
# with open('Data/prices.csv', 'rt') as file: 
#     count = 0
#     for line in file:
#         count += 1 
    
#     while count > 0: 
#         row = line.split(',')
#         record[row[0]] = float(row[1])
#         record = record  record[row[0]]
#         print(row)

#         count -= 1 


# prices = {} # Initial empty dict

# with open('Data/prices.csv', 'rt') as f:
#     for line in f:
#         row = line.split(',')
#         prices[row[0]] = float(row[1])

# print (prices)
# dic = {
#     'ne': 'Maher',
#     'pce': 23
# }

# dic2 = {
#     'na': 'Claire',
#     'address': 23
# }


# DicRes = dic.update(dic2)

# print(dic)
# print(dic2)

# print(DicRes)

# myInt = 5
# def addNumber(myInt):
#     myInt = myInt+10
#     print("Memory Address of myInt",id(myInt))
#     return myInt
    
# print(addNumber(myInt))
# print(myInt)
# print("Memory Address of myInt",id(myInt))

# Using Break
# ls = [1,2,3,4,5,6,7,8]

# for num in ls:
#     if num == 5:
#         continue
#     else: 
#         print("Hello")
#     line = 0
#     while line < 
#     for line in file:
    
#         row = line.split(',')
#         record[row[0]] = float(row[1])

# print(record)

# Test
#Zip Function

# row = ['name', 'address', 'value']
# col = ['abc', '2xx abc', 10]

# dicts = dict(zip(row, col))
# print(dicts)

#Value, Key pair
#Test

val = [('GOOG', 490.1), ('AA', 23.45), ('IBM', 91.1), ('MSFT', 34.23)]

print(sorted(val))
