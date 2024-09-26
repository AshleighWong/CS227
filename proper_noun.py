"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""

def find_proper_nouns(data: str) -> list[str]:
    """Function looking for proper nouns in a sentence."""
    proper = []
    data = data.split()
    for word in data:
        if word[0].isupper():
            proper.append(word)
    return proper
#End-of-file (EOF)
