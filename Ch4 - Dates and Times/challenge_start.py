# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar
# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

# This function counts the number of the given weekday for the
# specified year and month and returns the result
def countdays(theyear, themonth, whichday):
    daycount = 0
    weekslist = calendar.monthcalendar(theyear, themonth)
    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

print("--Day counter program--\n")

run = True
while run:
    try:
        print("Which day of the week do you want to count?"
              "\n1: Monday\n2: Tuesday\n3: Wednesday\n4: Thursday"
              "\n4: Friday\n6: Saturday\n7: Sunday\nOr 'exit' to quit")

        theday = input("? ")
        if theday == "exit":
            run = False
            break
        day = int(theday)-1
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))

        result = countdays(year, month, day)
        print("There are " + str(result) + " of "
              +calendar.day_name[day]+str(day)+" in the month and year specified")
        print("-----------\n")
    except Exception as e:
        print(e)
        print("That's not valid input")

