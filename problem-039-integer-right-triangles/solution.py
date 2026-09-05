# a + b + c = p 
# a^2 + b^2 = c^2 

# a^2 + b^2 = p^2 + a^2 + b^2 - 2pa - 2pb + 2ab 
#   2pa + 2pb - 2ab = p^2
#   (p^2 - 2pa) / 2(p-a) = b

# smallest is 3,4,5 (p = 12)
triangles = []
counts = {}

for p in range(12, 1001):
    counts[p] = 0
    for a in range(1, p//2+1):
        if (p**2 - 2*p*a) % (2*p - 2*a) == 0:
            b = (p**2 - 2*p*a) // (2*p - 2*a)
            c = p - a - b
        else:
            continue
        if a**2 + b**2 == c**2 and a > 0 and b > 0 and c > 0 and b>a:
            triangles.append([a, b, c])
            counts[p] += 1
        
    


ans_39 = max(counts, key=counts.get)
print(ans_39)
