# pcost.py       
with open('Data/portfolio.csv', 'rt') as file:
    total = 0.0
    rowCount = 0
    for row in file:
        if rowCount == 0: 
            print(row)
        else: 
            data = row.split(',')
            total = total + float(data[1]) * float(data[2])
        rowCount += 1 
    print("Total:", total)
# Exercise 1.27
