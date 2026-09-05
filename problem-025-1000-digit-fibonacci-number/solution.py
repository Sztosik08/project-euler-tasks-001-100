# --- Attempt 1 ---
#brute force
fibonaci = [1,1]
x = 0
len_of_last_idx = len(list(map(int, str(fibonaci[-1]))))
while len_of_last_idx != 1000:
    fibonaci.append(fibonaci[x]+fibonaci[x+1])
    x += 1
    len_of_last_idx = len(list(map(int, str(fibonaci[-1]))))
    
print(len(fibonaci))


# --- Attempt 2 ---
# "calculator" solution
import math
# because of the golden ratio fibonaci terms converge to n * Phi = n+1
# Phi is (1+sqrt5)/2
# 1000 digit number is 10**999
phi = (1 + math.sqrt(5))/2
# solve for idx_25 phi ** idx_25 / math.sqrt(5) >= 10 ** 999

#idx_25 * math.log(phi) - math.log(5)/2 > 999 * math.log(10)
idx_25 = (999 * math.log(10) + math.log(5)/2) / math.log(phi)
print(round(idx_25))
