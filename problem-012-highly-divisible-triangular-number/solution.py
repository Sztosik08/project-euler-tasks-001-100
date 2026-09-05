import math
p_12 = list(range(1,1000000))
triangular = []

for i in range(len(p_12)):
    triangular.append(sum(p_12[0:i+1]))
    num = triangular[-1]
    divisors = []
    for y in range(1, int(math.sqrt(num)) + 1):
        if num % y == 0:       # If 'i' is a divisor of 'num'
            divisors.append(y) # Add 'i' to the list of divisors
            # if y != num // y:
            #     divisors.append(num // y)  # Add the corresponding divisor
    if len(divisors) > 250:
        break


print(triangular[-1])
