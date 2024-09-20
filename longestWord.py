"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""

def longest_words(inputs, outputs):
    """Function checks for longest word in each line of txt and writes it to outfile."""
    with open(inputs, encoding="utf-8") as filename:
        with open(outputs, 'w', encoding="utf-8") as outfile:
            for line in filename:
                longest = ''
                line = line.replace("\n", "")
                words = line.split(' ')
                for word in words:
                    if len(word) > len(longest):
                        longest = word
                outfile.write(longest + "\n")

def main():
    '''Function to handle user input and call the longest_words function'''
    inputs = input("Enter the input file name:")
    outputs = input("Enter the output file name:")
    longest_words(inputs,outputs)


if __name__ == "__main__":
    main()
#End-of-file (EOF)
