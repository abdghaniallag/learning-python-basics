#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#
from builtins import print
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it
print(timedelta(days=365, minutes=30))

# TODO: print today' s date
print("today is", datetime.now())

# TODO: print today's date one year from now
print("One year from now the date will be:",datetime.now()+timedelta(days=365))

# TODO: create a timedelta that uses more than one argument

print("three weeks and tow days from now it will be:",datetime.now()+timedelta(weeks=3,days=2))
# TODO: calculate the date 1 week ago, formatted as a string
t=datetime.now()-timedelta(weeks=1)
print(t.strftime("the date one week ago was %A %d %B, %Y"))

### How many days until April Fools' Day?
today=date.today()
afd= date(today.year,4,1)
# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if today > afd :
    afd = afd.replace(year=today.year+1)


# TODO: Now calculate the amount of time until April Fool's Day  

print("time to next april's fools' day ",(afd-today).days)