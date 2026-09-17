f = open("problem-082-path-sum-three-ways/matrix.txt")
content = f.read()
raw_content = content.split()

grid = []
for line in raw_content:
    l = line.split(',')
    grid.append(list(map(int, l)))
    
    
cost = [[0]*80 for _ in range(80)]

# fill the first column with costs
for i in range(0,80):
    cost[i][0] = grid[i][0]
    


for j in range(1, 80):
    # seed column j from column j-1
    for i in range(0, 80):
        cost[i][j] = cost[i][j-1] + grid[i][j]

    # sweep down
    for i in range(1, 80):
        cost[i][j] = min(cost[i][j], cost[i-1][j] + grid[i][j])

    # sweep up
    for i in range(78, -1, -1):
        cost[i][j] = min(cost[i][j], cost[i+1][j]+grid[i][j])
        
answ = float('inf')

for nr in range(0,80):
    if cost[nr][79] < answ:
        answ = cost[nr][79]
        
print(answ)