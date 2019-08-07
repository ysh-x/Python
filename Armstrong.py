def armstrong(num):

    sum = 0
    temp = num 
    while num > 0:
        rem = int(num%10)
        dig = int(num/10)
        num = int(num/10)
        sum = sum+pow(rem,3)
        """
        print("REM: ",rem)
        print("DIG: ",dig)
        print("NUM: ",num)
        print("Sum: ",sum)
        """
        
        if temp == sum:
            print(temp,'IS AN ARMSTRONG NUMBER')


dummy = 101
while dummy <500:

    armstrong(dummy)
    dummy+=1
    
