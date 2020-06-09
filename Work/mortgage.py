import os
import importlib
from style import style

principle = float(input("How much is the mortage:")) 
mortage_years = int(input("How many years?:"))
rate = float(input("How much is the rate?:"))
extra_payment = float(input("How much is the extra payment"))
start_extra_payment_period = int(input("when do you want to start doing extra payments?"))
end_extra_payment_period = int(input("when do you want to finsih doing extra payments?"))

month = 1
totalRegularPayment = 0.0
totalExtraPayment = 0.0

monthly_payment = ((rate/100/12)/(1-(1+rate/100/12)**(-mortage_years*12)))*principle



while principle > 0:
    if principle <= monthly_payment+extra_payment:
            monthly_payment = principle * (1+rate/100/12)
            extra_payment = 0.0
            print("There is no need for an extra payment")

    principle = principle * (1+rate/100/12) - monthly_payment
    totalRegularPayment = totalRegularPayment + monthly_payment

    if month >= start_extra_payment_period and month <= end_extra_payment_period:
            principle = principle - extra_payment
            totalExtraPayment = totalExtraPayment + extra_payment           
           
    
    print( style.WHITE+'month:', month, style.RED+'Total Regular Payment:', totalRegularPayment, style.YELLOW+'Total Extra Payment:', totalExtraPayment, style.BLUE+'remaining principle:', principle)
    month += 1

totalPayment = totalRegularPayment + totalExtraPayment
print(style.MAGENTA+'Total Payment:',  totalPayment)
print(style.RESET)


