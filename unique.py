"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""

def unique_visitors(ids):
    """Function finds # of unique IDS and returns number."""
    sets = {}
    for num in ids:
        if len(num) == 8:
            if num in sets:
                sets[num] +=1
            else:
                sets[num] = 1
    return len(sets)
#End-of-file (EOF)
