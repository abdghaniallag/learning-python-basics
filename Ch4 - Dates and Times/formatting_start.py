#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    today = datetime.today()

    #### Date Formatting ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(today.strftime("Current date is %A %d %B %Y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(today.strftime("local time %X"))
    print(today.strftime("local date %x"))

    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(today.strftime("Time %H %M %S %ps"))


if __name__ == "__main__":
    main()
