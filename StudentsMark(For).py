Number = int(input("NUMBER OF STUDENTS: "))
i = 1
Sum = 0
for i in range(1,(Number+1),1):
    print("ENTER THE MARK[",i,"]: ")
    Mark = float(input())
    Sum = Sum+Mark
    Aver = Sum/Number
    i+=1
print("SUM: ",Sum)
print("AVERAGE: ",format(Aver,".2f"))

        
