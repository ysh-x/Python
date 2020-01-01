#Use of typeCast and String formatting 
number = (input("DECIMAL - "))
binary  = '0b'+number #Converting it into a python binary digit
binary_mod = str(int(number,2)) # TypeCasting binary to decimal and then to string # Slicing 'ob' from the string to avoid confusions
print(f"THE BINARY OF {number} is {binary_mod}") #Using string formatting to print the dynamic output