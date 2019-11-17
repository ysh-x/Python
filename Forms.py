def PrintDisp(S):  #This function creates the block for the strings
	Length = len(S)

	for i in range(0,Length+4): # This prints the upper deck of the block
		print("*",end="")

	print("")

	print("|",end="") 
	print(S,end="") # This prints the side deck of the block
	print("|")

	for i in range(0,Length+4): #This prints the lower deck of the block
		print("*",end="")

	print("\n")


#Getting the input of the block
name = input("NAME\t|")
age = input("AGE\t|")
gender = input("GENDER\t|")
maritial = input("STATUS\t|")
occupation = input("OCCUPATION\t|")
annualPay = input("ANNUAL PAY\t|")

#Inserting values in the block
List = [name,age,gender,maritial,occupation,annualPay]

#Arranging the strings 
PrintDisp(" \tBIO DATA \t")
PrintDisp("NAME\t| "+name)
PrintDisp("AGE\t| "+age)
PrintDisp("GENDER\t| "+gender)
PrintDisp("STATUS| "+maritial)
PrintDisp("OCCUPATION| "+occupation)
PrintDisp("ANNUAL PAY| "+annualPay)
