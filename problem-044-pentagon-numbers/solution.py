# --- Attempt 1 ---
import math

def f(x):
    return (x*(3*x-1))//2

pent_nrs = []
for x in range(1,1000000):
    pent_nrs.append(f(x))


# --- Attempt 2 ---
def is_pent_nr(n):
    k = (1 + math.sqrt(1 + 24*n)) / 6
    return k == int(k)


# --- Attempt 3 ---
print(pent_nrs[0:14])


# --- Attempt 4 ---
min_diff = float('inf')
for j in range(len(pent_nrs)):
    for k in range(j):
        diff = pent_nrs[j] - pent_nrs[k]
        if diff >= min_diff:
            break  
        if is_pent_nr(diff) and is_pent_nr(pent_nrs[j] + pent_nrs[k]):
            min_diff = diff


# --- Attempt 5 ---
print(min_diff)
