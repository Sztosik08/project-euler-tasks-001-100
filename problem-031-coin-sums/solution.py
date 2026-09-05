# nice to learn dynamic programming problem

coin_sum = 200
coins = [1,2,5,10,20,50,100,200]

ways = [0] * (coin_sum+1)
ways[0] = 1


for i in range(len(coins)):
    for j in range(len(ways)):
        if coins[i] <= j:
            ways[j] += ways[(int)(j-coins[i])]
            
print(ways[-1])
