# function to remove punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

Input = "Hello in 36-650, & other MSP courses."
Output = "Hello in 36650 other MSP courses"

# iterate through input string, and replace each punctuation by deleting, then print out final input string
def remove_punct(Input):
    for i in Input: 
        if i in punctuations:
            Input = Input.replace(i, "")
    print(Input)

remove_punct(Input)
