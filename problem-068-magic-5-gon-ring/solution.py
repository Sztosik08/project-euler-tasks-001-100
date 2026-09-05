# if we start indexing from the top lines can be defined as

# (outer1, inner1, inner2)
# (outer2, inner2, inner3)
# (outer3, inner3, inner4)
# (outer4, inner4, inner5)
# (outer5, inner5, inner1)

# we aim for 16digit string so 10 has to be an outer one and sums of lines have to be equal. then:

from itertools import permutations

# positions: [i1, i2, i3, i4, i5, o1, o2, o3, o4, o5]
# indices: [0,1,2,3,4,5,6,7,8,9]

# lines: (o1,i1,i2), (o2,i2,i3), (o3,i3,i4), (o4,i4,i5), (o5,i5,i1)
lines = [(5, 0, 1), (6, 1, 2), (7, 2, 3), (8, 3, 4), (9, 4, 0)]

perm = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# find all permutations which give the same sum of the positions of lines
solutions = []

for p in perm:
    target_sum = sum(p[idx] for idx in lines[0])

    if all(sum(p[idx] for idx in line) == target_sum for line in lines[1:]) and p.index(10) >= 5:
        
        solutions.append(p)

#generate lines
corr_lines = []
for sol in solutions:
    a = []
    for line in lines:
        a.append(tuple(sol[idx] for idx in line))
    corr_lines.append(a) 
    
# function to find the line with the smallest starting number
def find_1st_nr(line):
    idx = 0
    min_v = 11
    for l in line:
        if l[0] < min_v:
            min_v = l[0]
            idx = line.index(l)
    return idx


#loop to find the solution among viable line sequences
solution = 0 
for line in corr_lines:
    
    start = find_1st_nr(line)
    a = ""
    for nr in line[start]:
        a += str(nr)
    c_l_idx = start + 1
    while c_l_idx != start:
        if c_l_idx == 5:
            c_l_idx = 0
            continue 
        for nr in line[c_l_idx]:
            a += str(nr)
        c_l_idx += 1
    
    
    
    if len(a) == 16 and int(a) > solution:
        solution = int(a)

print(solution)
