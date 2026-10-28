# used: K = N - sum of factors + No. of factors

# so like that: K=4 - (2+2)+2 = 2


best = {}
LIMIT = 24000
KMAX = 12000

def search(product, total, count, start):
    if count >= 2:
        k = product - total + count
        if k <= KMAX:
            best[k] = min(best.get(k, float('inf')), product)
    for f in range(start, LIMIT+1):
        if product * f > LIMIT: 
            break
        search(product*f, total + f, count+1, f)


search(1, 0, 0, 2)

print(best)
print(f"answer is: {sum(set(best.values()))}")
    
