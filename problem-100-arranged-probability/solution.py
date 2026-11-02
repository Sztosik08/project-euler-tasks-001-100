


'''
so if b is number of blue discs and x is the number of total discs 
with x > 10 ** 12

we got to find such b * (b-1) == x * (x-1) * 50%

This equation can be solved algebraically - we omit the zero and negative solutions and land on:

b = 1 + sqrt(2x**2 - 2x + 1) / 2


'''

# Brute force solution presented below cannot be completed in reasonable time:

# bound = 10 ** 12
# x = bound + 1
# b = 1 + math.sqrt(2*x**2 - 2*x + 1) / 2

# while b.is_integer() == False:
#     if is_perfect_square((2*x**2 - 2*x + 1)):
#         b = (1 + math.sqrt(2*x**2 - 2*x + 1)) / 2
#     x +=1
    
# print(b)
# print(x)


# Let's use Pell Equation for that -> specifically negative Pell equation: u^2 - Dy^2 = -1

# first: 2x^2 - 2x + 1 must be a perfect square - that's our y^2
# then we complete the equation with u = 2x - 1

# and solutions of u^2 - 2y^2 = -1 come from multiplying (u + y*2**0.5) by (3 + 2**0.5)   

# and for each we get x = (u + 1) / 2 and b = (y+1) / 2


# we start with (u, y) == (1,1)

y = 1
u = 1
x = (u + 1)/2
b = (y+1)/2 

while x < 10 ** 12:
    # solutions of u^2 - 2y^2 = -1 come from multiplying (u + y*2**0.5) by (3 + 2**0.5) which gives us: (3u + 4y) + (2u + 3y)·√2
    u, y = 3*u + 4*y, 2*u + 3*y


    x = (u + 1)/2
    b = (y+1)/2 
print(f"Total: {int(x)}, answer is: {int(b)}")

