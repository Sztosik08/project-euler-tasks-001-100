# i used the build-in library 

from decimal import Decimal, getcontext
import math 

def sum_digs(n):
    suma = 0
    while n > 0:
        suma += n % 10 # extract last digit
        n //= 10 # remove last digit

    return suma

def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2


getcontext().prec = 105

total = 0

for i in range(1,101):
    if is_square(i):
        continue
    
    x = Decimal(i).sqrt()
    b = int(str(x)[2:101])
    total += sum_digs(b) + int(str(x)[0])
    

print(total)

