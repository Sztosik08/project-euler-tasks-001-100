# --- Attempt 1 ---
# let's think of it as ab / cd where I want to exclude the trivial examples so a, b, c, d != 0 

to_remove = [i for i in range(10,100,10)]


# possible fractions
nums_33 = [i for i in range(10,100) if i not in to_remove]
n_33 = []
d_33 = []

# numerator < denominator (because fractions have to be >1)
for num in nums_33:
    for den in nums_33:
        if num >= den:
            continue
        a, b = list(map(int, str(num)))
        c, d = list(map(int, str(den)))
        
        if a == c and num * d == den * b:
            n_33.append(b)
            d_33.append(d)
        if a == d and num * c == den * b:
            n_33.append(b)
            d_33.append(c)
        if b == c and num * d == den * a:
            n_33.append(a)
            d_33.append(d)
        if b == d and num * c == den * a:
            n_33.append(a)
            d_33.append(c)
               


# --- Attempt 2 ---
for n, d in zip(n_33, d_33):
    print(f"{n}/{d}")
    
import math
gcd_33 = math.gcd(math.prod(n_33), math.prod(d_33))
# we get 8 / 800 and GCD is 8
print(math.prod(d_33) // gcd_33)
# 800 / 8 = 100 :)
