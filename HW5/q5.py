def star_triangle(side):
    m = (2 * side) - 2
    for i in range(0, side):
        for j in range(0, m):
            print(end=" ")
        m = m - 1
        for j in range(0, i + 1):
            print("* ", end=' ')
        print(" ")

star_triangle(3)
