# report.py
# ------------------report2.4 
def report1():
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

#---------------------report2.5

def report2():
    def read_portfolio(filename):
            portfolio = [] 
            with open(filename, 'rt') as file:
                count = 0
                
                for row in file:               
                        if count == 0: 
                            header = row.split(',')
                        else:
                            dic = {} 
                            data = row.split(',')
                            dic[header[0]] = data[0]
                            dic[header[1]] = int(data[1])
                            dic[header[2]] = float(data[2])
                            portfolio.append(dic)
                           
                        count += 1
                        
            return portfolio
    print(read_portfolio('Data/portfolio.csv')) 

#----------------invoke report2.4:
report1()

#----------------invoke report2.5:
report2()
                                                                                                                                                                                                                               