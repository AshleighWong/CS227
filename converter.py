"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used pythonds3 textbook as a reminder of basic base conversion code.
"""
def number_converter(num, base=2):
    """
    Function to convert any decimal number to any base.
    """
    digits = "0123456789ABCDEF"
    stack = []
    if num == 0:
        return "0"
    while num > 0:
        rem = num % base
        stack.append(digits[rem])
        num = num // base
    #join instead of using a string and concatenating
    return ''.join(reversed(stack))
#End-of-file (EOF)
