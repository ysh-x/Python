#DATALIST
vowels = ['a','e','i','o','u'] 
cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','w','v','x','y','z']
numbers=[0,1,2,3,4,5,6,7,8,9]
VC = 0
CC = 0
NC = 0
OC = 0
#Input 
checkstring = input('STRING\t|')
checkString = checkstring.lower()


#Checking the data with the string check
for i in checkString:
	for j in vowels:
		if(i==j):
			VC = VC+1
			

for i in checkString:
	for k in cons:
		if(i==k):
			CC = CC+1
			


for i in checkString:			
	for l in numbers:
		if(i==l):
			NC = NC+1
#Formula for calculating the other charecters
OC = (len(checkString)-(VC+CC+NC))

#Printing the report
print("***************************************************************")
print('\t\t\tREPORT')
print("TOTAL LETTERS PRESENT IN THE GIVEN FEED\t|",len(checkString))
print("NUMBER OF VOWELS IN THE GIVEN FEED\t|",VC)
print("NUMBER OF CONSENENTS IN THE GIVEN FEED\t|",CC)
print("NUMBER OF NUMERICAL DIGITS IN THE FEED\t|",NC)
print("NUMBER OF OTHER CHARECTERS IN THE FEED\t|",OC)
print("***************************************************************")

