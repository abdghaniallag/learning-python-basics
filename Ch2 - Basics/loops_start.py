#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    """
    while (x < 7) :
        print(x)
        x = x+1  
    """
    # TODO: define a for loop
    """
        for x in range(5,10):
        print(x)
    """

    # TODO: use a for loop over a collection
    """
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in days:
        print(d)
    """
    # TODO: use the break and continue statements
    """
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
       if(d=="Sat"):
            break
       if(d=="Tue"):
            continue
       print(d)

    """
    # TODO: using the enumerate() function to get index 
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate( days):
       print(i,d)

  
if __name__ == "__main__":
    main()
