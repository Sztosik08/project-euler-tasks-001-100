# --- Attempt 1 ---
# n from r - there's proba
import math
def n_from_r(n, r):
    return (math.factorial(n))//(math.factorial(r)*(math.factorial(n-r)))

counter = 0

for n in range(1,101):
    for r in range(0,n+1):
        if n_from_r(n,r) > 1000000:
            counter +=1

print(counter)


# --- Attempt 2 ---
# quicker
count_v2 =0
for n in range(1,101):
    for r in range(0,n+1):
        if math.comb(n,r) > 1000000:
            count_v2 +=1
print(count_v2)
