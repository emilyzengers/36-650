# function to print number triangle
def num_triangle(rows):
    # initialize starting number
    number = 1
    # outer loop to iterate number of rows
    for i in range(0, rows):
        # inner loop to iterate number of columns
        for j in range(0, i + 1):
            print(number, end = ' ')
            number = number + 1
        # print line break to create new row
        print("\r")

num_triangle(3)
