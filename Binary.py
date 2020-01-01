#Use of typeCast and String formatting 
number = int(input("DECIMAL - "))
binary  = str(bin(number)) # TypeCasting decimal to binary and then to string
binary_mod = binary[2:] # Slicing 'ob' from the string to avoid confusions
print(f"THE BINARY OF {number} is {binary_mod}") #Using string formatting to print the dynamic output