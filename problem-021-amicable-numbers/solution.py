def find_sum_proper_divisors(n):
    divisors = [1]
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

amicable_nr = []
for i in range(1, 10001):
    a = find_sum_proper_divisors(i)
    b = find_sum_proper_divisors(a)
    if b == i and a != b:
        amicable_nr.extend([a,b])

amicable_nr = list(dict.fromkeys(amicable_nr))
print(sum(amicable_nr))
