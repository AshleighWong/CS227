"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""

def is_leap(year):
    """Function checking leap years."""

    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    return leap

def main():
    '''Function to handle user input and call the is_leap function'''
    year = 0
    while year < 1000 or year > 10000:
        year = int(input("input year between 1000 and 10000: "))
    print(is_leap(year))


if __name__ == "__main__":
    main()
#End-of-file (EOF)
