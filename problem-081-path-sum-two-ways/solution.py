f = open("problem-081-path-sum-two-ways/matrix.txt")
content = f.read()
raw_content = content.split()

grid = []
for line in raw_content:
    l = line.split(',')
    grid.append(list(map(int, l)))
    

grid_s = [[0]*80 for _ in range(80)]

grid_s[0][0] = grid[0][0]



# filling 1st row
for j in range(1, 80):
    grid_s[0][j] = grid[0][j] + grid_s[0][j-1]
#filling 1st column
for i in range(1, 80):
    grid_s[i][0] = grid[i][0] + grid_s[i-1][0]
    
for i in range(1,80):
    for j in range(1,80):
        grid_s[i][j] = grid[i][j] + min(grid_s[i-1][j], grid_s[i][j-1])
        
print(grid_s[79][79])

