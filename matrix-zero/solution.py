import numpy as np
def setZero(Matrix):
    row = [0 for i in range(len(Matrix))]
    columns = [0 for i in range(len(Matrix[0]))]
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            if Matrix[i][j] == 0:
                row[i] = 1
                columns[j] =1

    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            if row[i] == 1 or columns[j] == 1:
                Matrix[i][j] = 0

Matrix = [  [1,2,1,5],
            [1,1,1,1],
            [4,1,0,6],
            [2,1,3,1]]
print(np.array(Matrix))
setZero(Matrix)
print(np.array(Matrix))
