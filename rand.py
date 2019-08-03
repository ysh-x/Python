import random

def roll():
    a = [1,2,3,4,5,6]
    print("YOU HAVE GOT",random.choice(a))
        
while True:
    
    print(' ROLL ? ')
    choice=input()
    if(choice == 'y' or 'Y'):
         roll()
    elif(choice == 'n' or 'N'):
        print('EXIT')
        break
        
    
