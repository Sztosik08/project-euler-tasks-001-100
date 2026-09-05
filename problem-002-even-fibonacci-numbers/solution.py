# --- Attempt 1 ---
fibonaci = [1,2]
for x in range(100000):
    fibonaci.append(fibonaci[x]+fibonaci[x+1])
    if fibonaci[-1] >= 4000000:
        fibonaci.remove(fibonaci[-1])
        break
    
print(fibonaci[-1])


# --- Attempt 2 ---
sum_even = 0
even_list = []
for x in range(len(fibonaci)):
    if fibonaci[x] % 2 == 0:
        sum_even += fibonaci[x]
        even_list.append(fibonaci[x])
    
print(sum_even)
print(even_list)
