# --- Attempt 1 ---
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

# # Convert number to list of integers
# digits = list(map(int, str(50)))

# # 1. Convert each number to a string
# # 2. Join them together
# # 3. Cast the final string to an integer
# result = int("".join(map(str, digits)))


# --- Attempt 2 ---
n = 3797
lis = []

digits = list(map(int, str(n)))
while len(digits) > 0:
    lis.append(int("".join(map(str,digits))))
    digits.pop(-1)
    
digits = list(map(int, str(n)))
while len(digits) >0:
    lis.append(int("".join(map(str,digits))))
    digits.pop(0)


# --- Attempt 3 ---
n = 11 #next prime after 7 
primes_37 = []
lis = []

while len(primes_37) != 11:
    digits = list(map(int, str(n)))
    while len(digits) > 0:
        lis.append(int("".join(map(str,digits))))
        digits.pop(-1)
    
    digits = list(map(int, str(n)))
    while len(digits) >0:
        lis.append(int("".join(map(str,digits))))
        digits.pop(0)
    
    lis = list(set(lis))
    if all(isPrime(y) for y in lis) == True:
        primes_37.append(n)
    lis = []
    n += 1
    while isPrime(n) == False:
        n +=1
    
print(sum(primes_37))  
    


# --- Attempt 4 ---
print(primes_37)
print(sum(primes_37))
