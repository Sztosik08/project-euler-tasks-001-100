import math

def is_perfect_square(n):
    if n < 0:
        return False
    else:
        root = int(math.sqrt(n))
        return root * root == n




# # tried brute force initially but failed (for some the x is astronomically largr)
# def get_min_solution(d):
#     if is_perfect_square(d):
#         return False
#     x = 1

#     while True:
#         for y in range(1,x):
#             if x**2 - d*y**2 == 1:
#                 return x
                
#         x +=1


# another approach - the minimal solution is always found in the convergents of D**0.5 continued fraction :o

# we already got this from previous task
def get_period_sq(n):
    a0 = int(n**0.5)
    if a0**2 == n:  # perfect square
        return 0, []
    
    a = a0
    m = 0
    d = 1
    period_count = 0
    period = []
    is_period = False
    
    while is_period==False:
        m = d * a - m
        d = (n - m**2) // d
        a = (a0 + m) // d 
        
        period.append(a)
        period_count += 1
        
        if a == 2 * a0:
            is_period = True
    
    return period


def get_min_sol2(d):
    if is_perfect_square(d):
        return None
    a0 = int(d**0.5)
    h_prev, h_curr = 1, a0    
    k_prev, k_curr = 0, 1
    
    period = get_period_sq(d) 
    i = 0
    while True:
        a = period[i % len(period)]
        h_prev, h_curr = h_curr, a * h_curr + h_prev
        k_prev, k_curr = k_curr, a * k_curr + k_prev
        
        if h_curr**2 - d * k_curr**2 == 1:
            return h_curr
        i += 1


max_x, d = 0, 0

for i in range(2,1001):
    cand = get_min_sol2(i)
    if cand == None:
        continue
    if cand > max_x:
        max_x, d = cand, i
        
print(d)
