#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#
from wsgiref.validate import validator


def main():
    x, y = 1000, 100

    # conditional flow uses if, elif, else
    if x < y :
      result = "x is less than y"
    elif x == y:
      result = "x is the same as y"
    else :
      result = "x is greater than y"

    # conditional statements let you use "a if C else b"
    result= "x is less than y" if x<y else "x is equal to or greater than y"
    # match-case makes it easy to compare multiple values


    value = "five"
    match value:
        case "one":
            result="choice one"
        case "two":
            result="choice two"
        case "three":
            result="choice three"
        case _:
            result="undefined"
    print(result)

if __name__ == "__main__":
    main()
