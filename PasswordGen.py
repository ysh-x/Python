#DATALIST
import random
vowels = ['a','e','i','o','u'] 
cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','w','v','x','y','z']
#Getting inputs
n = int(input("NUMBER OF BYTE TERMS\t|"))
x = int(input("NUMBER OF PASSWORDS REQUIRED\t|"))

#Template[One Consonent - One Vowel and Other Non Vowel and Again a Vowel]
for i in range(0,x):
	print("________________________________________________________")
	print("PASSWORD NUMBER ",i+1)
		
	for j in range(0,n):
		print(cons[random.randrange(0,20,1)],end="")
		print(vowels[random.randrange(0,5,1)],end="")
		print(cons[random.randrange(0,20,1)],end="")
		print(vowels[random.randrange(0,5,1)],end="")
		print('-',end="")
	
	print()
	