# --- Attempt 1 ---
# okay now we may use some functions from the previous task :)
# this time we want to minimise the totient function which could be minimised 
# n/function will be minimised when n is a product of some larger primes 

def is_permutation(a,b):
    return sorted(list(str(a))) == sorted(list(str(b)))


# --- Attempt 2 ---
print((10**7)**0.5)


# --- Attempt 3 ---
to_check = primes_less_than(4000)
mn_ratio = float('inf')
mn_n = 0

for i in range(len(to_check)):
    for j in range(i+1, len(to_check)):
        p = to_check[i]
        q = to_check[j]
        n = p * q
        if n > 10**7:
            break  
        phi = (p-1) * (q-1)
        if is_permutation(phi, n) and n/phi < mn_ratio:
            mn_ratio = n/phi
            mn_n = n

print(mn_n)
