Number = int(input("NUMBER OF STUDENTS: "))
i = 1
SumEven = 0
SumOdd = 0
EvenCount = 0
OddCount = 0
while i <= Number:
    print("ENTER THE MARK[",i,"]: ")
    Mark = float(input())
    if(i%2==0):
        SumEven = SumEven+Mark
        EvenCount+=1
    else:
        SumOdd = SumOdd+Mark
        OddCount+=1
    
    i+=1

EvenAver = SumEven/EvenCount
OddAver = SumOdd/OddCount
print("SUM OF EVEN ROLL NUMBER: ",SumEven)
print("SUM OF ODD ROLL NUMBER: ",SumOdd)
print("AVERAGE OF EVEN ROLL NUMBER: ",EvenAver)
print("AVERAGE OF ODD ROLL NUMBER: ",OddAver)


        
