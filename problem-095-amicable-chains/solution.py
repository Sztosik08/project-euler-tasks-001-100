# build a sieve of divisors sum (excl the number itself from it's divisors sum)
import numpy as np

sums = np.zeros(1000001, dtype=np.int64)

for d in range(1,500001):
    for i in range(2*d, len(sums), d):
        sums[i] += d
        
# Helper - get_chain from the sums of divisors

def get_chain(start):
    chain = [start]
    
    cont = True
    
    while cont:
        next = sums[chain[-1]]
        if next >= 1000000 or next == 0:
            return None
        if next in chain:
            cont = False
        else:
            chain.append(next)
    
    if chain[0] == sums[chain[-1]]:       
        return chain
    else:
        return None
    
    
len_chain = 0
longest_chain = []

for i in range(1, 1000000):
    ch = get_chain(i)
    if ch == None:
        continue
    else:
        if len(ch) > len_chain:
            len_chain = len(ch)
            longest_chain = ch
        
print(f"The answer is: {min(longest_chain)}")