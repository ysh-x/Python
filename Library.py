fine = 0
expectedDate = float(input("EXPECTED DATE: "))
expectedMonth = float(input("EXPECTED MONTH: "))
expectedYear = float(input("EXPECTED YEAR: "))

actualDate = float(input("RETURNED DATE: "))
actualMonth = float(input("RETURNED MONTH: "))
actualYear = float(input("ACTUAL YEAR: "))

if(expectedYear == actualYear and expectedMonth == actualMonth):
    if(expectedDate>=actualDate):
        fine = 0
    else:
        fine = 15*(actualDate-expectedDate)
        
elif(expectedYear == actualYear):
    fine = 500*(actualMonth-expectedMonth)
else:
    fine = 10000

if(fine==0):
    print("THANKS FOR RETURNING THE BOOK ON TIME")
else:
    print("I AM SORRY! YOU WERE NOT ON TIME. YOUR FINE IS RS:",fine)
