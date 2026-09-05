def is_Palindrome(n):
    return list(map(int, str(n))) == list(map(int, str(n)))[::-1]

def reverse(n):
    return int(str(n)[::-1])


lychrel_n = 0

for i in range(1, 10001):
    curr_its = 0
    a = i
    is_lychrel = True
    while curr_its < 50:
        b = reverse(a)
        a += b
        if is_Palindrome(a):
            is_lychrel = False
            break
        curr_its +=1
    if is_lychrel:
        lychrel_n +=1
print(lychrel_n)
