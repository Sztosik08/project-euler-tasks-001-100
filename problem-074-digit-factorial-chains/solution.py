# --- Attempt 1 ---
import math


def factorial_nrs(n):
    x = 0
    for d in str(n):
        x +=math.factorial(int(d))
    return x

def produce_chain(n):
    chain = [n]
    curr_nr = factorial_nrs(n)
    while True:
        if curr_nr not in chain:
            chain.append(curr_nr)
        else:
            break
        curr_nr = factorial_nrs(curr_nr)
    
    return chain 


# --- Attempt 2 ---
answ = 0
for i in range(1,10**6):
    if len(produce_chain(i)) == 60:
        answ +=1


# --- Attempt 3 ---
print(answ)
