# ok - brute force approach will be too slow and with 10^9 floats might fail 

# let's see - with (a, a, b) [with b = a +/- 1]:
    # the height is math.sqrt(a^2 - b^2/4) so the area is b * math.sqrt(4a^2 − b^2)/4
    
    
# to solve this it's the Pell equation used also in problem 100



X, m = 2, 0

bound = 10**9

perimeter_s = 0

while True:
    X, m = 2*X + 3*m, X+2*m
    
    if X % 3 == 1:
        perimeter = X-2
    elif X % 3 ==2:
        perimeter = X +2
    else:
        continue
    
    if perimeter > bound:
        break
    
    
    
    if perimeter <= 2:
        continue
    
    perimeter_s += perimeter
    
print(perimeter_s)
