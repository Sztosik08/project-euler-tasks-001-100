f = open("problem-083-path-sum-four-ways/matrix.txt")
content = f.read()
raw_content = content.split()

grid = []
for line in raw_content:
    l = line.split(',')
    grid.append(list(map(int, l)))
    
    
dist = [[float("inf")]*80 for _ in range(80)]
visited = [[0]*80 for _ in range(80)]
dist[0][0] = grid[0][0]

frontier = [(dist[0][0], (0,0))]

neighbour_cords = [(-1,0), (1,0), (0, -1), (0,1)]

while frontier:
    c_min = min(frontier)
    cost, (r, c) = c_min

    frontier.remove(c_min)
    
    if visited[r][c] == 1:
        continue
    visited[r][c] = 1
    
    for cord in neighbour_cords:
        nr, nc = r + cord[0], c + cord[1]
        if nr < 0 or nr >= 80 or nc < 0 or nc >= 80:
            continue
        if cost + grid[nr][nc] < dist[nr][nc]:
            dist[nr][nc] = cost + grid[nr][nc]
            frontier.append((dist[nr][nc], (nr,nc)))
    
print(dist[79][79])   

