# report.py

portfolio = []
def read_portfolio(filename): 
    
    with open(filename, 'rt') as file:
        next(file)
        for row in file:
                #First Method
                data = row.split(',')
                # data = [data[0], int(data[1]), float(data[2])]
                # tup_data = tuple(data)
                #Second Method to Generate Tuple:
                data = (data[0], int(data[1]), float(data[2]))
                portfolio.append(data)
    return portfolio



print(read_portfolio('Data/portfolio.csv')) 

 


                                                                                                                                                                                                                               