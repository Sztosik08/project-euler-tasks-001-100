# digits:
    # 1 digit = 9 * 1 
    # 2 digit = 90 * 2 
    # 3 digit = 900 * 3 
    # 4 digit = 9000 * 4
    # 5 digit = 90000 * 5
    # 6 digit = 900000 * 6
    # total 5888889 digits

# suma = 9 * (1 + 10*2 + 100*3 + 1000*4 + 10000*5 + 100000*6)
# print(suma)

fraction_list = []

for n in range(1, 1000000):
    digits = list(map(int, str(n)))
    for digit in digits:
        fraction_list.append(digit)
        
indexes = [0, 9, 99, 999, 9999, 99999, 999999]

ans_40 = 1
for indx in indexes:
    ans_40 *= fraction_list[indx]
    
print(ans_40)
