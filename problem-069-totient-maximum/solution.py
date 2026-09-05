# --- Attempt 1 ---
from functools import reduce

def factors(n):
    return list(set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


def relative_primes(a, b):
    if b < a:
        a, b = b, a 
    a_factors = factors(a)
    b_factors = factors(b)
    common_factors = []
    for item in a_factors:
        if item in b_factors:
            common_factors.append(item)
            if len(common_factors) > 1:
                return False
    
    if len(common_factors) == 1:
        return True

def totient(n):
    y = []
    for i in range(1,n):
        if relative_primes(i, n):
            y.append(i)
    return(y)

def totient_val(n):
    y = 0
    for i in range(1,n):
        if relative_primes(i, n):
            y +=1
    return(y)

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
a = primes_less_than(1000000)

total = 2
for n in a:
    if n == 2:
        continue
    total *= n
    if total >= 1000000:
        print(total)
        print(total // n)
        break
