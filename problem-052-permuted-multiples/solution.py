def same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))
    


print(same_digits(125874, 125874*2))


# we can create bounds so that if I got x and 6x they contain the same number of digits 
upper_b_for6 = 999999//6
upper_b_for7 = 9999999//6
upper_b_for5 = 99999//6


for a in range(100000, upper_b_for6):
    if all(same_digits(a, a*x) for x in range(2, 7)):
        print(a)
        break
