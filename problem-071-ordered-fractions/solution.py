
# brute force almost cause following Farey sequence if a/b and c/d are adjacent fractions then bc - ad = 1

# so if n/d is a neighbour of 3/7 then 3d - 7n = 1 so n = 3d-1/7 or d = 

import math

viable = []

for d in range(1,1000001):
    n = (3*d - 1) // 7
    if math.gcd(n,d) ==1 and n/d < 3/7:
        viable.append([n, d, n/d])
        

answ = 0
m = 0
for l in viable:
    if l[2] > m:
        m = l[2]
        answ = l[0]
        
print(answ)


# another way -> maximise d so that it's the closest to 1 000 000

viable_d = 0
for d in range(1000000, 0, -1):
    if (3*d - 1) % 7 == 0:
        viable_d = d
        n = (3*d - 1) // 7
        break
    
print(f"d is: {viable_d}")
print(f"answer is: {n}")