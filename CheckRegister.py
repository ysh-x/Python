RegisterNumber = input("Word :")
registerNumber = RegisterNumber.upper()
print("GIVEN ID : ",registerNumber)
P = registerNumber.split()
P1 = registerNumber[0:2]
P2 = registerNumber[2:5]
P3 = registerNumber[5:9]

if(P1.isdigit()==True and P2.isalpha()==True and P3.isdigit()==True):
    print("VALID VIT ID")
    if(int(P1)==19 and P2=='MIS' and int(P3)>1000):
        print("IT BELONGS TO YOUR CLASS")
    else:
        print("IT DOES NOT BELONGS TO YOUR CLASS")
 
else:
    print("INIVALID VIT ID")
    
