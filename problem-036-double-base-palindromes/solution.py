def isPalindrome(n):
    res = list(map(int, str(n)))
    last_to_1st = []
    for i in res[::-1]:
        last_to_1st.append(i)
    if res == last_to_1st:
        return True
    else:
        return False


ans_36 = []
for i in range(1, 1000001):
    if isPalindrome(i) == True:
        if isPalindrome(int(format(i, 'b'))) == True:
            ans_36.append(i)
    else:
        continue
  
print(sum(ans_36))
