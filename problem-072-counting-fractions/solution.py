# this is the sum of the totient functions (problem 69) phi(2) to phi(1000000)

phi = list(range(1000001))
for p in range(2, 1000001):
    if phi[p] == p: 
        for multiple in range(p, 1000001, p):
            phi[multiple] -= phi[multiple] // p
            
print(sum(phi[2:1000001]))