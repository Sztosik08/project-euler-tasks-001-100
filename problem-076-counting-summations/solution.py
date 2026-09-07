

# similar to problem 31
# nice to learn dynamic programming problem

int_sum = 100
ints = [i for i in range(1, 100)]

ways = [0] * (int_sum+1)
ways[0] = 1


for i in range(len(ints)):
    for j in range(len(ways)):
        if ints[i] <= j:
            ways[j] += ways[(int)(j-ints[i])]
            
print(ways[-1])

