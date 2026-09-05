# --- Attempt 1 ---
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False    
    return True

def isPandigital(n):
    n_digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if list(set(list(map(int, str(n))))) == n_digit[0:len(str(n))]:
        return True
    else:
        return False
    
    


# --- Attempt 2 ---
a =4214124

print(list(map(int, str(a)))[-1])


# --- Attempt 3 ---
pandigital_primes = []
for i in range(1, 7654322):
    if list(map(int, str(i)))[-1] in [2, 4, 5, 6, 8, 0]:
        continue
    if isPandigital(i) == True:
        if isPrime(i) == True:
            pandigital_primes.append(i)
    else:
        continue


# --- Attempt 4 ---
print(pandigital_primes)
