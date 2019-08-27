s = input("Word :")
print('STRING FUNCTIONS'.center(70,'-'))
print('First Letter as a capital :',s.capitalize())
print('Upper case of the word    :',s.upper())
print('Lower case of the word    :',s.lower())
print('Formatting')
print(s.center(70))
print(s.center(70,'-'))
print('String to be used for comparision :',s.casefold())
parameter = input("Parameter : ")
print("Parameter",parameter)
print('Occurance :',s.count(parameter))
print('Occurance :',s.count(parameter,1,5))
print('Ends with :',s.endswith(parameter))
print('Ends with :',s.endswith(parameter,1,9))
print('Found at the index :',s.find(parameter))        
print('Found at the index :',s.index(parameter))
print('Is Aplhanumeric ? :',s.isalnum())



print('-'.center(70,'-'))


