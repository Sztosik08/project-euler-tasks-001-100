# normal solution

def find_triplet(total):
    for a in range(1, total // 3):
        for b in range(a + 1, total - a):
            c = total - a - b
            if b < c and a * a + b * b == c * c:
                return a, b, c
    return None

triplet = find_triplet(1000)

if triplet is not None:
    a, b, c = triplet
    print(triplet)
    print(a * b * c)


# funny solution
import math
import random

a_9 = 0
b_9 = 0

while a_9 + b_9 + math.sqrt(a_9 ** 2 + b_9 ** 2) != 1000:
    a_9 = random.randint(1,501)
    b_9 = random.randint(1,501)
    
print(a_9)
print(b_9)
print(math.sqrt(a_9 ** 2 + b_9 ** 2))
