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



my_primes = primes_less_than(1000000)
i = 10


while my_primes[i]**2 + 8 + 16 < 50000000:
    i += 1
  
  
primes_a = my_primes[0:i]

i = 10
while 4 + my_primes[i]**3 + 16 < 50000000:
    i +=1

primes_b = my_primes[0:i]

i = 10
while 4 + 8 + my_primes[i]**4 < 50000000:
    i +=1

primes_c = my_primes[0:i]


done = []

for c in range(0, len(primes_c)):
    for b in range(0, len(primes_b)):
        for a in range(0, len(primes_a)):
            curr = primes_a[a]**2 + primes_b[b]**3 + primes_c[c]**4
            if curr > 50000000:
                break 
            if curr < 50000000:
                done.append(curr)

                
print(len(set(done)))
