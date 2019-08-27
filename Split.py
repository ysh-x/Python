String = input("STRING:")
deLimiter = input("DELIMITER:")
listString = (String.split(deLimiter))

for x in range(0,len(listString),1):
    print(listString[x])
    print('')
