import math


def has_integer_route(a, b, c):
    return is_square_int((a+b)**2 + c**2)

def is_square_int(n):
    if n < 0:
        return False
    root = int(math.isqrt(n)) 
    return root * root == n

"""

here essentially s = a + b:

we know that a <= b

so a <= s // 2

b = s - a <= c
so a >= s - c

and a >=1

so a ranges from max(1,s-c) to s // 2

"""


M = 0
count = 0

while count < 1_000_000:
    M +=1 
    c = M
    for s in range(2, 2*c +1):
        if is_square_int(s**2 + c**2):
            count += max(1, s//2 - max(1, s - c) + 1)


print(count)
print(f"answer is: {M}")