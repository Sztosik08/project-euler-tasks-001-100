#check for the upper bound

import matplotlib.pyplot as plt
import math
def f(x):
    return sum(math.factorial(int(c)) for c in str(x))
x = range(0, 10000001)
y = [f(i) for i in x]
plt.figure(figsize=(12, 6))
plt.plot(x, y, linewidth=0.5)
plt.xlabel("X")
plt.grid(True)

plt.show()


# visualization is nice but let's check the numbers themselves

# 7-digit number
print(f(9999999))

# 8-digit number
print(f(99999999))

# 9-digit number
print(f(999999999))

# i wouldn't go beyond the 7-digit number - the sums are not growing much beyond that 


f_of_dig = []

for i in range(10, f(9999999)+1):
    if i == f(i):
        f_of_dig.append(i)
        
print(f_of_dig)


print(sum(f_of_dig))
