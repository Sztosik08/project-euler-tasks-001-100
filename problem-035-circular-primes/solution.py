# --- Attempt 1 ---
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

# 5 also cannot be here but i just left 5 here for simplicity of the function 
def oddDigits(n):
    for i in list(map(int, str(n))):
        if i%2==0:
            return False

    return True

def rotate_digits(num):
    rotations = [num]
    num_list = [c for c in str(num)]
    for i in range(1, len(num_list)):
        rotations.append(int(''.join(num_list[i:] + num_list[:i])))


    return rotations


# --- Attempt 2 ---
circ_primes = [2]

for i in range(1,1000001):
    if isPrime(i) == True and oddDigits(i) == True:
        rots = rotate_digits(i)
        if all(isPrime(y) for y in rots) == True:
            circ_primes.append(i)


# --- Attempt 3 ---
print(circ_primes)
print(len(circ_primes))
