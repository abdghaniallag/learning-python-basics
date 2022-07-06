#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#
from datetime import time
from datetime import date
from datetime import datetime


def main():
    # DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class

    today = date.today()
    # print("Today is ",today)
    # TODO: print out the date's individual components
    # print("day {} moth {} year {}".format(today.day,today.month,today.year))
    # print("Today's weekday ", today.weekday())
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    # days =["sat","sun","mon","tue","wed","thu","fri"]
    # print("Today's weekday ",days[today.weekday()])

    
    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    # todaynow=datetime.now()
    # print("current datetime is ",todaynow)
    
    # TODO: Get the current time
    print(datetime.time(datetime.now()))
 

  
if __name__ == "__main__":
    main()
  