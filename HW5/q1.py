# function to transpose matrix
X = [[10, 8],
    [2, 4],
    [1, 7]]

# nested list and for loop
def transpose_matrix(X):
    Y = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    for k in Y:
        print(k)

transpose_matrix(X)