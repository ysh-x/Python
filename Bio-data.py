#------------BIO DATA ( FULL) ---------------------------#
name = input('NAME : ')
age = int(input('AGE : '))
father = input("FATHER'S NAME : ")
mother = input("MOTHER'S NAME : ")
gender = input("GENDER :")
phone = int(input("PHONE : "))
number = int(input("ENTER THE NUMBER OF SUBJECTS "))
mark1 = int(input(" MARK 1 : "))
mark2 = int(input(" MARK 2 : "))
mark3 = int(input(" MARK 3 : "))
mark4 = int(input(" MARK 4 : "))
mark5 = int(input(" MARK 5 : "))
sume = (mark1+mark2+mark3+mark4+mark5)
average = sume/5

if(average>=90):
     result = "DISTINTION"
elif(average>=80):
      result = "GOOD"
elif(average>=70):
     result = "AVERAGE"
else:
    result = "POOR"
         
      

#-----------------PRINTING--------------------------------#

print("/n/n")           
print("+------------------------BIO-DATA---------------+")
print("NAME : ",name)
print("AGE: ",age)
print("FATHER'S NAME : ",father)
print("MOTHER'S NAME : ",mother)
print("GENDER : ",gender)
print("PHONE : ",phone)
print("NUMBER OF SUBJECTS : ",number)
print("MARK 1 : ",mark1)
print("MARK 2 : ",mark2)
print("MARK 3 : ",mark3)
print("MARK 4 : ",mark4)
print("MARK 5 : ",mark5)
print("SUM : ",sume)
print("AVERAGE : ",average)
print("PERCENTAGE : ",average,"%")
print("CLASS : :",result)
            
            
print("+------------------------BIO-DATA---------------+")
