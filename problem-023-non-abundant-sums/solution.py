# --- Attempt 1 ---
def find_sum_proper_divisors(n):
    divisors = [1]
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def is_abundant(n):
    x = find_sum_proper_divisors(n)
    if x > n:
        return True
    else:
        return False

def is_not_aboundant(n):
    x = find_sum_proper_divisors(n)
    if x > n:
        return False
    else:
        return True
    


# --- Attempt 2 ---
# find aboundant numbers
aboundant_nrs = []
for i in range(1, 28123):
    if is_abundant(i) == True:
        aboundant_nrs.append(i)
        
other_nrs = []
for i in range(1,28123):
    if is_not_aboundant(i) == True:
        other_nrs.append(i)


# --- Attempt 3 ---
sum_of_aboundant = []
for i in range(0,len(aboundant_nrs)):
    for x in range(i,len(aboundant_nrs)):
        product_aboundant = aboundant_nrs[i] + aboundant_nrs[x]
        if product_aboundant <= 28123:
            sum_of_aboundant.append(product_aboundant)
        


# --- Attempt 4 ---
answers_23 = []
for i in range(1,28124):
    if i not in sum_of_aboundant:
        answers_23.append(i)
        


# --- Attempt 5 ---
print(sum(answers_23))
