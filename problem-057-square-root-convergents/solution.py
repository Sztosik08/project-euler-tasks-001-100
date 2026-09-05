# --- Attempt 1 ---
# we got:
#   - 3/2
#   - 7/5
#   - 17/12
#   - 41/29

# so the reccurences for numerator (n) and denominator (d) are:
    # n2 = n1 + 2 * d1
    # d2 = n1 + d1
    
count = 0
nums = [3]
dens = [2]

for i in range(0, 1001):
    n = nums[-1] + dens[-1] *2
    d = nums[-1] + dens[-1]
    nums.append(n)
    dens.append(d)
    if len(str(n)) > len( str(d)):
        count +=1

print(count)


# --- Attempt 2 ---
for i in range(4):
    print(nums[i], dens[i])
