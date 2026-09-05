# --- Attempt 1 ---
x = 600851475143

divisors = []
for i in range(1,int(x**0.5)+1):
    if x % i == 0:
        divisors.append(i)
        if i != x // i:
            divisors.append(x // i)

print(divisors)


# --- Attempt 2 ---
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True


# --- Attempt 3 ---
primes_of_divisors = []
for number in divisors:
    if isPrime(number) == True:
        primes_of_divisors.append(number)

print(max(primes_of_divisors))
