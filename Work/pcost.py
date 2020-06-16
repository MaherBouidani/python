# pcost.py       
def portfolio(filename): 
    total = 0.0
    with open(filename, 'rt') as file:
        rowCount = 0
        for row in file:
            if rowCount == 0: 
                print(row)
            else: 
                data = row.split(',')
                total = total + float(data[1]) * float(data[2])
            rowCount += 1
    return total

cost = portfolio('Data/portfolio.csv')
print("Total:", cost)
# Exercise 1.27
