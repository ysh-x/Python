print('ENTER YOU AGE ')
age = int(input())
if(age>18):
    print('ELIIBLE TO VOTE')
else:
    remain=18-age
    print('YOU HAVE ',remain,' YEAR(S) STILL TO VOTE')
