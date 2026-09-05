# --- Attempt 1 ---
# for e we got 2 and then series where at index 1,3,4,6,7,9,10 etc we got 1 and at index 2,5,8,11 we got 2,4,6,8

def nth_coef_of_e(n):
    if n == 0:
        return 2
    if n%3 ==2:
        return (n+1)//3 *2
    else:
        return 1


# --- Attempt 2 ---
#numerator n = an * n_-1 + n_-2
n_0 = 2
n_1 = 3

for i in range(2,100):
    a = nth_coef_of_e(i)
    n = a * n_1 + n_0
    n_0, n_1 = n_1, n
    
    
    
print(sum(list(map(int, str(n)))))
