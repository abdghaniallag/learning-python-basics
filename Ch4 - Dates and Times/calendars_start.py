#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#

# TODO: import the calendar module


import calendar
import os

# TODO: create a plain text calendar


Calendar = calendar.TextCalendar(calendar.SUNDAY)
# str=Calendar.formatmonth(2022,1,0,0)
# print(str)
# TODO: create an HTML formatted calendar
# htmlForma =calendar.HTMLCalendar(calendar.SUNDAY)
# str=htmlForma.formatmonth(2022,1)
# print(str)
# index=open("index.html","w+")
# index.write(str)
# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for day in Calendar.itermonthdays(2022,8):
#     print(day)

# TODO: The Calendar module provides useful utilities for the given locale,
#  such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)
for day in calendar.day_name:
    print(day)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for month in range(1,13):
    cal=calendar.monthcalendar(2022,month)
    weekOne=cal[0]
    weekTow=cal[1]
    if weekOne[calendar.FRIDAY] != 0:
        meetDay = weekOne[calendar.FRIDAY]
    else :
        meetDay = weekTow[calendar.FRIDAY]
    print(calendar.month_name[month],  meetDay)