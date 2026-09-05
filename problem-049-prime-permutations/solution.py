import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False    
    return True

def is_permutation(a, b):
    a = list(map(int,str(a)))
    b = list(map(int,str(b)))
    if sorted(a) == sorted(b):
        return True


primes_4 = []
for i in range(1000,10000):
    if isPrime(i):
        primes_4.append(i)
        


permutations_4 = []
for i in range(len(primes_4)):
    curr_perm = [primes_4[i]]
    x = primes_4[i]
    for n in range(i+1, len(primes_4)):
        y = primes_4[n]
        if is_permutation(x, y) == True:
            curr_perm.append(y)
    if len(curr_perm) >=3:
        permutations_4.append(curr_perm)
        curr_perm = []
    else:
        curr_perm = []
        continue


from itertools import combinations
solution = []
for per in permutations_4:
    for j in combinations(per, 3):
        if 1487 not in j:
            if sorted(j)[2] - sorted(j)[1] == sorted(j)[1] - sorted(j)[0]:
                solution.append(j)
            
print(solution)


for item in solution:
    print(''.join(map(str, item)))
