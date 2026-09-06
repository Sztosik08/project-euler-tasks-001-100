# brute force

import math

viable = 0

for d in range(2,12001):
    for n in range(d//3 +1, (d-1)//2+1):
        if math.gcd(n,d) == 1:
            viable +=1

print(viable)
