# --- Attempt 1 ---
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False    
    return True

def isPerfectSquare(n):
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n


# --- Attempt 2 ---
# solution 1 with a bound on the i (squared number)

def is_Goldbach(n):
    if n%2 == 0:
        return False
    if isPrime(n):
        return False
    for x in range(1,n+1):
        if isPrime(x) == False:
            continue
        else:
            for i in range(1, int(math.sqrt(n/2)) + 1):
                if 2*i**2 + x == n:
                    return True
                else:
                    continue
    return a


# --- Attempt 3 ---
# faster solution without a loop on the i

def is_Goldbach(n):
    if n%2 == 0:
        return False
    if isPrime(n):
        return False
    for x in range(1,n):
        if isPrime(x) == False:
            continue
        else:
            remainder = n - x
            if remainder % 2 == 0 and isPerfectSquare(remainder//2):
                return True
    return a


# --- Attempt 4 ---
a = 9

while is_Goldbach(a) !=a:
    a+=2
    
print(a)
