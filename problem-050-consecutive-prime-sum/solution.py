# --- Attempt 1 ---
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False    
    return True


# --- Attempt 2 ---
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


# --- Attempt 3 ---
primes_50 = sorted(list(set(primes_less_than(1000000)) - set(primes_less_than(1000))))
all_primes = primes_less_than(1000000)


# --- Attempt 4 ---
# my sums of primes to quickly calculate the sums of primes 
prefix = [0] * (len(all_primes)+1)

for i in range(len(all_primes)):
    prefix[i+1] = prefix[i] + all_primes[i]


# --- Attempt 5 ---
print(prefix)
print(all_primes)


# --- Attempt 6 ---
print(sum(all_primes[0:6]))
print(prefix[6]-prefix[0])


# --- Attempt 7 ---
prime = 0
counter = 0

for i in range(len(all_primes)):
    for l in range(1, len(all_primes)):
        if i+l >= len(prefix):
            break
        s = prefix[i+l] - prefix[i]
        
        if s > 1000000:
            break
        if isPrime(s) and l > counter:
            prime = s
            counter = l 


# --- Attempt 8 ---
print(prime, counter)
