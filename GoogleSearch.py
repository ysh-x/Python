
from googlesearch import search
print("\n\n\n\n\n\n")
Term = input("EXPLORE THE WEB ")
print("\n\n\n\n\n")
Results = search(Term,tld="com",lang="en",num=10,start=0,stop=10,pause=2.0)

print("\t\t\tTOP HITS")
for i in Results:
	print("YOUR TOP HIT : ",i)