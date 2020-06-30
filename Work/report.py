# report.py
# ------------------report2.4 
import csv

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

#---------------------report2.5 Interview Type Code
def report2():
    portfolios = []
    total = 0.0 
    def read_portfolios(filename):
            
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
                            portfolios.append(dic)
                           
                        count += 1
                        
            return portfolios
    print(read_portfolios('Data/portfolio.csv'))

    for portfolio in portfolios:
        total += portfolio['shares'] * portfolio['price\n']
    print (total) 

#---------------------report2.5 Work Type Code

def report3():
    portfolios = []
    def read_portfolios(filename):
            
            with open(filename, 'rt') as file:
                rows = csv.reader(file)
                header = next(rows)             
                for row in rows:                                      
                            dic = {} 
                            dic[header[0]] = row[0]
                            dic[header[1]] = int(row[1])
                            dic[header[2]] = float(row[2])
                            portfolios.append(dic)
                           
                        
            return portfolios          
    def total():
        total = 0.0
        for portfolio in portfolios:
            total += portfolio['shares'] * portfolio['price']
        return total

    portResult = read_portfolios('Data/portfolio.csv')
    totalRes = total()
    return portResult, totalRes
       
    #Note: Return Method could return multiple values in Python. The Default return type is a "TUPLE"
    #and could be "LIST" if specified <return [,]> 
    #------To Calcualte all the total investments: 
    
#----------------report 2.6 
def report4(): 
    def read_prices(filename):
            
            with open(filename, 'rt') as file:
                rows = csv.reader(file)
                next(rows)
                dic = {}             
                for row in rows:                                                             
                    dic[row[0]] = row[1].strip()                                                
            return dic
    dicResult = read_prices('Data/prices.csv')
    reportReturn , totalResult = report3()
    print(totalResult)
    #Direct calculation of the new total without updating the data with the new shares prices list
    total = 0.0
    for portfolio in reportReturn:
        total += portfolio['shares'] * float(dicResult[portfolio['name']])
    print(total)
    
#Updating the data with the new shares prices list:    
    # Issue -2, Reduce the big(O) to O(N) by direct access updating
    # for portfolio in reportReturn:
    #     portfolio['price'] = float(dicResult[portfolio['name']])

    # Issue -2, the orignial method of O(n2)
    # for key in dicResult:
    #     count = 0   // Enhancement: use enumerate(reportReturn) to puropse count and k,v,e at the same time
    #     for k,v,e in reportReturn:
    #         if key == reportReturn[count][k]:
    #             reportReturn[count][e] = float(dicResult[key])
    #         count += 1
    # total = 0.0
    # for portfolio in reportReturn: 
    #     total +=  portfolio['shares'] * portfolio['price']
    
    # print(total)
    if total > totalResult: 
        print("Gain=", total - totalResult)
    else: 
        print("Loss=", abs(total - totalResult))
    





#----------------invoke report2.4:
# report1()

#----------------invoke report2.5:
# report2()

#----------------invoke report2.5:
# report3()
#----------------invoke report2.6
report4()
                                                                                                                                                                                                                               