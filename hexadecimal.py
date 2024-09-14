"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""

def hex_plus_one(digits: list[str]) -> list[str]:
    """Function that increments hexadecimal list by 1."""
    hexa = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(digits)-1, -1, -1):
        if digits[i] not in hexa and int(digits[i]):
            if digits[i] == '9':
                digits[i] = 'A'
            else:
                digits[i] = str(int(digits[i])+1)
                return digits
        else:
            if digits[i] == 'F':
                digits[i] = '0'
            else:
                digits[i] = hexa[hexa.index(digits[i]) + 1]
                return digits
    return ['1'] + digits
#End-of-file (EOF)
