def armstrong(Number):
    Sum = 0
    temp = Number
    while Number > 0:
        rem = int(Number%10)
        dig = int(Number/10)
        Number = int(Number/10)
        Sum =  Sum+pow(rem,3)
        #print("Sum: ",Sum)
        if(Sum==temp):
            print(temp,"IS AN ARMTRONG NUMBER")

Number = int(input("ENTER THE NUMBER: "))
armstrong(Number)
   
