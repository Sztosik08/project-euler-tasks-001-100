# --- Attempt 1 ---
def isPandigital(n):
    if len(list(map(int, str(n)))) != 9:
        return False
    if list(set(list(map(int, str(n))))) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    else:
        return False

def firstDigit(n):
    while n >= 10: 
        n = n / 10
    return int(n)


# --- Attempt 2 ---
# we look for the largest number so we only take into account numbers starting with 9
mults = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nrs = list(range(1,10000))
nrs = [x for x in nrs if firstDigit(x) == 9]
ans_38 = []

for nr in nrs:
    for i in range(0,10):
        x = ""
        for mul in mults[0:i+1]:
            x += str(nr * mul)
        if isPandigital(int(x)):
            ans_38.append(int(x))
        


# --- Attempt 3 ---
print(max(ans_38))
