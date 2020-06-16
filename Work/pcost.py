# pcost.py 
      
#--------------------
# in case we want to pass the filename as an argument from the terminal: 
#import sys
#--------------------

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

# ------------------------------------------------------------------ 
# If passing the filename as an arugument from the terminal command:
# if len(sys.argv) == 2: 
#    filename = sys.argv[1]
# else: 
#    filename = 'Data/portfolio.csv'
# ------------------------------------------------------------------

cost = portfolio('Data/portfolio.csv')
print("Total:", cost)
# Exercise 1.27
