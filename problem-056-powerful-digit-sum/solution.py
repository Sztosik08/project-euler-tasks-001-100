digit_sum = 0
for a in range(1,101):
    for b in range(0,101):
        x = a**b
        x = sum(list(map(int, str(x))))
        if x > digit_sum:
            digit_sum = x
    
print(digit_sum)
