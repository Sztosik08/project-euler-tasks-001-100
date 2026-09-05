# --- Attempt 1 ---
divisors_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ,20]


def divisor_check(cur_n, divs):
    for div in divs:
        if cur_n % div != 0:
            return False
    print(cur_n)
    return True


# --- Attempt 2 ---
#brute force solution
for i in range(2, 1000000000):
    if divisor_check(i, divisors_5) == True:
        break


# --- Attempt 3 ---
#sol 2
import math
from functools import reduce 

# def lcm(a,b):
#     return int(((a*b) / math.gcd(a,b)))

result = reduce(math.lcm, range(1,21))
print(result)
