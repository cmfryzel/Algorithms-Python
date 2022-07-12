import numpy as np

def dfs(grid, rows, cols):
    numRows = len(grid)
    numCols = len(grid[0])
    
    if(rows<0 or cols<0 or rows>=numRows or cols>=numCols or grid[rows][cols]==0):
        return
    
    grid[rows][cols]=0
    dfs(grid, rows-1, cols)
    dfs(grid, rows+1, cols)
    dfs(grid, rows, cols-1)
    dfs(grid, rows, cols+1)

def remIslands(grid):
    newMat = grid
    x = len(grid)
    y = len(grid[0])
    for i in range(x):
        for j in range(y):
            if(i==0):
                dfs(grid, i, j)
            elif(i==x-1):
                dfs(grid, i, j)
            elif(j==0):
                dfs(grid, i, j)
            elif(j==y-1):
                dfs(grid, i, j)
    return np.subtract(newMat,grid)
            




m = [
[1, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 1],
[0, 0, 1, 0, 1, 0],
[1, 1, 0, 0, 1, 0],
[1, 0, 1, 1, 0, 0],
[1, 0, 0, 0, 0, 1]
]
print(remIslands(m))
