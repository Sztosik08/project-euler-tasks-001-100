from functools import reduce 

# print(result1_6)
result1_6 = sum(map(lambda i: i*i, range(1,101)))
print(result1_6)
result2_6 = sum(range(1,101))**2
print(result2_6)

print(f"final result: {result2_6-result1_6}")


n_6 = 100

square_of_sum = n_6 ** 2 * (n_6+1) ** 2 * 1/4
sum_of_squares = n_6 * (n_6+1) * (2*n_6+1) * 1/6

print(square_of_sum)
print(sum_of_squares)

print(f"result is: {square_of_sum-sum_of_squares}")
