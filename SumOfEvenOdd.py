Number = int(input("NUMBER OF STUDENTS: "))

SumEven = 0
SumOdd = 0
for i in range(1,(Number+1),1):
    print("ENTER THE MARK[",i,"]: ")
    Mark = float(input())
    if(Mark%2==0):
        SumEven = SumEven+Mark
    else:
         SumOdd = SumOdd+Mark
        
print("SUM OF EVEN MARKS: ",SumEven)
print("SUM OF ODD MARKS: ",SumOdd)

        
