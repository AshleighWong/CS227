"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""

def duplicates(names):
    """Function finds duplicate names and returns a list of them."""
    dic= {}
    for name in names:
        if name not in dic:
            dic[name] = 1
        else:
            dic[name] += 1
    duplicated = []
    for key, value in dic.items():
        if value > 1:
            duplicated.append(key)
    return duplicated
#End-of-file (EOF)
