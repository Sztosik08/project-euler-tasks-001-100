
# narrowing the scope to avoid pure bruteforce :) :
#   because n=0 for 1st iteration the function f(n) = n**2 + an + b gives b for n=0 so b has to be a prime

def function_27(n, a, b):
    return n**2 + a*n + b

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

b_27 = []
for i in range(1001):
    if isPrime(i) == True:
        b_27.append(i)
        

# now we check possible pairs for f(1) = 1 + a + b 

pairs_27 = []
for item in b_27:
    for i in range(-999, 1000):
        if isPrime(function_27(1, i, item)) == True:
            pairs_27.append((i, item))

        



#consecutive primes 
cons_primes = []
for pair in pairs_27:
    n_of_primes = 0
    for i in range(0, 1000):
        if isPrime(function_27(i, pair[0], pair[1])) == True:
            n_of_primes += 1
        else:
            cons_primes.append(n_of_primes)
            break



max_cons_primes = max(cons_primes)

index_of_primes = cons_primes.index(max_cons_primes)

answer_27 = pairs_27[index_of_primes][0] * pairs_27[index_of_primes][1]
print(answer_27)
