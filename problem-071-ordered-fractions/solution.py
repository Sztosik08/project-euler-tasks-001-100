best_n, best_d = 0, 1

for d in range(1, 1000001):
    n = (3*d - 1) // 7
    if n * best_d > best_n * d:  # cross multiply to avoid floats
        best_n, best_d = n, d

print(best_n)


# brute force

import math

viable = []

for d in range(1,1000001):
    n = (3*d - 1) // 7
    if math.gcd(n,d) ==1 and n/d < 3/7:
        viable.append([n, d, n/d])
        
print("hello")


answ = 0
m = 0
for l in viable:
    if l[2] > m:
        m = l[2]
        answ = l[0]
        
print(answ)
