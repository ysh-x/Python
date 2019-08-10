NumberComputer = int(input("NUMBER OF COMPUTERS: "))
Costcomputer = int(input("COST OF ONE PIECE: "))
NumberTable = int(input("NUMBER OF TABLES: "))
CostTable = int(input("COST OF ONE TABLE: "))
NumberChair = int(input("NUMBER OF CHAIR: "))
CostChair = int(input("COST OF ONE CHAIR: "))
Hours = int(input("HOURS WORKED ?"))
Wages = int(input("WAGES: "))
TotalComp = Costcomputer*NumberComputer
TotalTable = NumberTable*CostTable
TotalChair = NumberChair*CostChair
Totallabour = Hours*Wages

print("+------------------------------------------------+")
print("|","PARTICULAR\t|","NUMBER\t|RATE\t|TOTAL\t","|")
print("|","COMPUTER:\t|",NumberComputer,"|\t",Costcomputer,"|\t",TotalComp,"|")
print("|","TABLE:\t|",NumberTable,"|\t",CostTable,"|\t",TotalTable,"|")
print("|","CHAIR:\t|",NumberChair,"|\t",CostChair,"|\t",TotalChair,"|")
print("|","LABOUR:\t|",Hours,Wages,"|\t",Totallabour,"|")
print("+------------------------------------------------+")
