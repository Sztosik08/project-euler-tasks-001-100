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


# --- Attempt 2 ---
# what does the problem tells me about the numbers:
#   - cannot start with a leading 0 
#   - I won't loop through the last digit cause it cannot be: 0, 2, 4, 5, 6, 8

# I need to enumerate all subsets of digit positions (excluding the last). For a 6-digit primes I got 5 non-last positions



# on divisilibity by three:
     #  If I replace 3 digits and the number is not divisible by 3 I won't get a number divisible by 3 
    


# --- Attempt 3 ---
from itertools import combinations
positions_6 = list(combinations(range(5), 3))  # exclude last position (5)
print(positions_6)


# --- Attempt 4 ---
# try the 6 digit numbers
full_set = primes_less_than(1000000)
primes_5digits = primes_less_than(100000)
prime_set = list(set(full_set) - set(primes_5digits))
prime_set = sorted(prime_set)

# create an list of all primes where i switch digits from give combinatinos (positions_6)
nr_combinations = []

for prime in prime_set:
    digits = list(map(int, str(prime)))
    for subset in positions_6:
        comb = []
        remaining = [digits[i] for i in range(6) if i not in subset]
        if sum(remaining) % 3 == 0:
            continue
        for i in range(0, 10):
            a = digits.copy()
            for number in subset:
                a[number] = i
            comb.append(a)
        nr_combinations.append(comb)
        


# --- Attempt 5 ---
# check in possibilities where do I have 8 primes 

possibilities = []
for c in nr_combinations:
    counter = 0
    if c[0][0] == 0:
        continue
    for nr in c:
        if isPrime(int("".join(map(str, nr)))):
            counter +=1
    if counter == 8:
        possibilities.append(c)


# --- Attempt 6 ---
# find the minimum value as I had duplicates
minim = 999999
for p in possibilities:
    for nr in p:
        nr = int("".join(map(str, nr)))
        if nr < minim:
            minim = nr
print(minim)
