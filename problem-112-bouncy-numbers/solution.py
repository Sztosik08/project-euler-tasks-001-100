def is_increasing(n):
    a = list(map(int, str(n)))
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return False
    return True

def is_decreasing(n):
    a = list(map(int, str(n)))
    for i in range(1, len(a)):
        if a[i-1] < a[i]:
            return False
    return True

def is_bouncy(n):
    if is_increasing(n):
        return False
    elif is_decreasing(n):
        return False
    else:
        return True
    
n = 100 #first bouncy number is 101 so we start at 100
bouncy_c = 0
ratio = 0

while ratio != 0.99:
    n +=1
    if is_bouncy(n):
        bouncy_c +=1
    ratio = bouncy_c/n

print(ratio)
print(n)