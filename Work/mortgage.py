

principle = float(input("How much is the mortage:")) 
mortage_years = int(input("How many years?:"))
rate = float(input("How much is the rate?:"))
extra_payment = float(input("How much is the extra payment"))
start_extra_payment_period = int(input("when do you want to start doing extra payments?"))
end_extra_payment_period = int(input("when do you want to finsih doing extra payments?"))

count = 1
totalPaid_after_extraPayment = 0.0
totalPaid = 0.0

monthly_payment = ((rate/100/12)/(1-(1+rate/100/12)**(-mortage_years*12)))*principle

while principle > 0:
    if principle <= monthly_payment+extra_payment:
            monthly_payment = principle * (1+rate/100/12)
            extra_payment = 0.0
            print("There is no need for an extra payment")

    if count >= start_extra_payment_period and count <= end_extra_payment_period:
            principle = (principle * (1+rate/100/12)) - (monthly_payment+extra_payment)
            totalPaid_after_extraPayment = totalPaid_after_extraPayment + (monthly_payment+extra_payment)
    else:                  
           principle = principle * (1+rate/100/12) - monthly_payment
           totalPaid = totalPaid + monthly_payment
    
    print( 'month:', count, ':','total paid:', totalPaid, 'total paid with extra:', totalPaid_after_extraPayment,'remaining principle:', principle)
    count += 1

totalPayment = totalPaid + totalPaid_after_extraPayment

print('total payment:', totalPayment)
