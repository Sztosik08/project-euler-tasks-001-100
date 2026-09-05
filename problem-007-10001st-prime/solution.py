primes_7 = []
i = 2 

while len(primes_7) < 10001: 
    if isPrime(i):
        primes_7.append(i)
    i += 1
    
print(primes_7[-1])
