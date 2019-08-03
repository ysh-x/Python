amount = float(input("Bob ! How much do you have ?"))
pricey  = float(input("Bob ! Turn the product an enter the price - "))
number = int(input("Bob ! How much choclate you ate and have the wrappers with you ?"))
choco = amount//pricey
freechoco = choco//number
if(pricey>amount):
    print('\n\nI am sorry Bob! You do not have sufficient amount for buying chocoloates')
else:
    print("\n\nCongratulations Bob! You can buy ",format((freechoco+choco),'.0f'),"Chocolates")

             
