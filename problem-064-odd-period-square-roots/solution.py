import math

def is_perfect_square(n):
    return math.sqrt(n) == math.floor(math.sqrt(n))


# we start with a_0 which is the 1st int in the sequence and a_0 = int(n**0.5)

# then a_i+1 = ((a_0+m_i+1)/d_i+1) where:
#   d_i+1 = (n - m_i+1**2) / d_i
#   m_i+1 = d_i * a_i - m_i

# we start with m_0 = 0; d_0 = 1 and a_0 = int(n**0.5)


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
    
    return period_count, period


count = 0

for i in range(1, 10001):
    if get_period_sq(i)[0] % 2 != 0:
        count +=1

print(count)
