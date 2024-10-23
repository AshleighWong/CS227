"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""

def average_grade():
    """Function takes the name and average of grades and write them to another file."""
    inputs = input("Enter the input file name: ")
    outputs = input("Enter the output file name: ")
    with open(inputs, 'r', encoding="utf-8") as filename:
        string = ''
        for line in filename:
            # line = line.replace("\n", "")
            words = line.split(' ')
            avg = 0
            for i,num in enumerate(words):
                if i == 0:
                    string = string + num + ' '
                else:
                    avg += int(num)
            avg = avg/(len(words)-1)
            string = string + str(avg) + "\n"
    with open(outputs, "w", encoding="utf-8") as outfile:
        outfile.write(string)

average_grade()
#End-of-file (EOF)
