Hours = int(input("HOURS BROWSED: "))
Mins = int(input("MINUTES BROWSED: "))

if(Hours>=7 and Mins==0):
    print("LIMIT EXCEDED !")
    Total = "N/A"
elif(Hours>=5):
    CostHour =(200+(Hours-5)*50)
    CostMin = Mins*1
    Total = CostHour+CostMin
else:
    CostHour =((Hours*50))
    CostMin = Mins*1
    Total = CostHour+CostMin
print("\n\n\n")
print("+---------------BROWSING BILL-----------------------+")    
print("|HOURS:\t",Hours,"|MINUTES:\t",Mins,"|COST:\t|",Total)
print("+---------------------------------------------------+")    
