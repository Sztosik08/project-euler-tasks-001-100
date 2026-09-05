# --- Attempt 1 ---
# if we got base and exp: for example base = 9 exp = 2 then base**exp = 81
# we can see that if base >= 10 then the base**exp always has more digits then exp is

# So base is in range 1-9


# --- Attempt 2 ---
base = 9
exp = 1
while len(str(base**exp)) == exp:
    exp +=1
upper_boud = exp

counter = 0
for exp in range(1,upper_boud):
    for base in range(1,10):
        if len(str(base**exp)) == exp:
            counter +=1
print(counter)
