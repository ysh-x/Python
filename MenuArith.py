numberOne = int(input("NUMBER 1: "))
numberTwo = int(input("NUMBER 2: "))
print("1. ADD/2. SUBRACT\n3. MULTIPLY\n4. DIVIDE\n5. MODULUS\n6. POWER")
choice = int(input())
if(choice==1):
    print("THE ANSWER IS: ",(numberOne+numberTwo))
elif(choice==2):
    print("THE ANSWER IS: ",(numberOne-numberTwo))
elif(choice==3):
    print("THE ANSWER IS: ",(numberOne*numberTwo))
elif(choice==4):
    print("THE ANSWER IS: ",(numberOne/numberTwo))
elif(choice==5):
    print("THE ANSWER IS: ",(numberOne%numberTwo))
elif(choice==6):
    print("THE =ANSWER IS: ",format((numberOne**numberTwo),".5f"))
else:
    print("UNDEFINED OPERATION")
    
