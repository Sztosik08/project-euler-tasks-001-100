# every Pythagorean triple can be generated using:

# a = m^2 - n^2 ; b = 2mn ; c = m^2 + n^2:

# where m > n > 0 ; gcd(m,n) = 1 ; one is even and one is odd
# So L = a + b + c = 2m^2 + 2mn = 2m(m+n)
import math

counts = [0] * 1500001

for m in range(2, 1500001):
    for n in range(1, m):
        if math.gcd(m,n) == 1 and (m+n)%2==1:
            L = 2*m*(m+n)
            if L > 1500000:
                break
            for i in range(L, 1500001, L):
                counts[i] += 1
 
total = 0               
for c in counts:
    if c == 1:
        total +=1
print(total)

# to clafiry the method with m and n produces PRIMITIVE triples:
# A primitive triple is a Pythagorean triple where a,b,c share no common factor i.e. gcd(a,b,c) == 1