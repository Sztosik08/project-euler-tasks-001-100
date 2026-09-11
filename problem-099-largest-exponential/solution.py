# Obtain data from the file :) 

f = open("problem-099-largest-exponential/base_exp.txt")
content = f.read()
raw_content = content.split('\n')

els = []

for line in raw_content:
    l = line.split(',')
    l = list(map(int, l))
    els.append(l)

# Actual solution :)) 

# a^b > c^d   <--->  b * log(a) > d * log(c)  

import math
max_id = 0

for i in range(len(els)):
    if math.log(els[i][0]) * els[i][1] > math.log(els[max_id][0]) * els[max_id][1]:
        max_id = i
        
print(f"answer is: {max_id+1}")
