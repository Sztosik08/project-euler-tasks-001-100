#similar problem to:

#problem 31
# nice to learn dynamic programming problem

# coin_sum = 200
# coins = [1,2,5,10,20,50,100,200]

# ways = [0] * (coin_sum+1)
# ways[0] = 1


# for i in range(len(coins)):
#     for j in range(len(ways)):
#         if coins[i] <= j:
#             ways[j] += ways[(int)(j-coins[i])]
            
# print(ways[-1])

def primes_less_than(n):
    if n<=2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for x in range(i*i,n,i):
                is_prime[x] = False
    
    return [i for i in range(n) if is_prime[i]]

# let's try an upper bound of 300 at first - should do 
primes = primes_less_than(300)
ways = [0] * (300 +1)
ways[0] = 1

for p in primes:
    for j in range(p, 300 + 1):
        ways[j] += ways[j - p]
for p in primes:
    ways[p] -= 1  # remove the single-prime sums
    
    
for item in ways:
    if item > 5000:
        print(f"answer: {ways.index(item)}")
        break
