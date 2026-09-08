# one can use a generating function for P(n) which gives the number of ways of writing the integer n as a sum of positive integers

# item 11 from https://mathworld.wolfram.com/PartitionFunctionP.html


my_ks = []
for n in range(1,1000):
    my_ks.append(n)
    my_ks.append(-n)

def pent(n):
    return (n*(3*n-1))//2

P = [1]
n = 1
while True:
    p_n = 0
    for i, k in enumerate(my_ks):
        pent_k = pent(k)
        if pent_k > n:
            break
        sign = (-1) ** (i // 2)
        p_n += sign * P[n - pent_k]
    P.append(p_n % 1000000)
    if P[n] == 0:
        print(n)
        break
    n += 1


