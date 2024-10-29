"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""
def checkout_lines(carts):
    """
    Function to process grocery store checkout and return total processing time.
    """
    if not carts:
        return 0
    checkout = [0, 0, 0]
    time = 0
    customer = 0
    while customer < len(carts) or any(checkout):
        for i in range(3):
            if checkout[i] == 0 and customer < len(carts):
                checkout[i] = carts[customer]
                customer += 1
        for i in range(3):
            if checkout[i] > 0:
                checkout[i] -= 1
        time += 1
    return time +2
#End-of-file (EOF)
