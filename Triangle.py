print("TYPE OF TRIANGLE")
print("1. ORTHODOX TRIANGLE")
print("2. RIGHT ANGLE TRIANGLE")
choice = float(input())
if(choice == 1):
    print("BREADTH: ")
    breadth = float(input())
    print("HEIGHT : ")
    height = float(input())
    area=(0.5*breadth*height)
    print("AREA : ",+area)  
elif(choice == 2):
    print("LEG 1: ")
    leg1 = float(input())
    print("LEG 2 : ")
    leg2 = float(input())
    area1=((leg1+leg2)/2)
    print("AREA : ",+area1)
else:
    print("WRONG CHOICE ")
    
