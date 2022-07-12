def search(matrix, n, m, x):
    numX = 0
    i = 0
    j = m-1
    while(i<n and j>=0):
        if(matrix[i][j]==x):
            numX+=1
        if(matrix[i][j]>x):
            j-=1
        else:
            i+=1
    return numX

mat = [
    [1, 4, 7, 12, 15, 1000],
    [2, 6, 19, 31, 32, 1001],
    [3, 7, 24, 33, 35, 1002],
    [7, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]
target = 7
rows=len(mat)
cols=len(mat[0])

print(search(mat,rows,cols,target))