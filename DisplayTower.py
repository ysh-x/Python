#
S = input("CONTENT TO PRINT IN THE TOWER\t|") # Get the content of the tower
C = int(input('ROWS IN THE TOWER \t|')) 
S1 = S.upper()
C = C+1

#Tower Loop constains
print('DISPLAY\t|')
for i in range(0,C):
	for j in range(i,0,-1):
	
			print(S1,"|",end="")

	print("\n")
