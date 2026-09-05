import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False    
    return True

def distinct_factors(n):
    factors = []
    i = 2

    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1

    if n > 1:
        factors.append(n)
    return list(set(factors))


nr_47 = []
a = 646
while len(nr_47) < 4:
    if len(distinct_factors(a)) == 4:
        nr_47.append(a)
    else:
        nr_47 = []
    a+=1


print(nr_47)


for number in nr_47:
    print(distinct_factors(number))
