# --- Attempt 1 ---
f = open("0067_triangle.txt")
content = f.read()
raw_content = content.split()

row_nr = 0
index = 0



triangle67 = []
for i in range(1, 101):
    unit67 = []
    row_nr += i
    unit67 = list(map(int, raw_content[index:row_nr]))
    triangle67.append(unit67)
    index = row_nr
    


# --- Attempt 2 ---
print(triangle67)


# --- Attempt 3 ---
for r in range(len(triangle67)-2, -1, -1):
    for j in range(r + 1): triangle67[r][j] += max(triangle67[r+1][j], triangle67[r+1][j+1])

print(triangle67[0][0])
