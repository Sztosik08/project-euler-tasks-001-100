# --- Attempt 1 ---
import math
# sieve of eratosthenes
def primes_less_than(n):
    if n<=2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for x in range(i*i,n,i):
                is_prime[x] = False
    
    return [i for i in range(n) if is_prime[i]]

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False    
    return True

def pairs_with(a,b):
    return isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a)))


# --- Attempt 2 ---
test_primes = primes_less_than(10001)

valid_test_pairs = []

for a in range(len(test_primes)):
    for b in range(a+1, len(test_primes)):
        if pairs_with(test_primes[a],test_primes[b]):
            valid_test_pairs.append([test_primes[a],test_primes[b]])
            
# build dictionary
pairs_dict = {}
for p in test_primes:
    pairs_dict[p] = set()
    
for a, b in valid_test_pairs:
    pairs_dict[a].add(b)
    pairs_dict[b].add(a)

valid_triples = []
for a, b in valid_test_pairs:
    # only check primes that pair with a and b
    candidates = pairs_dict[a] & pairs_dict[b]  # set intersection
    for c in candidates:
        if c > b:
            valid_triples.append([a, b, c])

valid_fours = []
for a,b,c in valid_triples:
    candidates = pairs_dict[a] & pairs_dict[b] & pairs_dict[c]
    for d in candidates:
        if d > c:
            valid_fours.append([a,b,c,d])

valid_fives = []
for a,b,c,d in valid_fours:
    candidates = pairs_dict[a] & pairs_dict[b] & pairs_dict[c] & pairs_dict[d]
    for e in candidates:
        if e > d:
            valid_fives.append([a,b,c,d,e])
            
print(valid_fives)
for item in valid_fives:
    print(sum(item))
