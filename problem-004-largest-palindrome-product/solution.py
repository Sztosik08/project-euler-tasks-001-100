def isPalindrome(n):
    res = list(map(int, str(n)))
    last_to_1st = []
    for i in res[::-1]:
        last_to_1st.append(i)
    if res == last_to_1st:
        return True
    else:
        return False


palindromes = []
for i in range(10, 1000):
    for x in range(100,1000):
        if isPalindrome(i*x) == True:
            palindromes.append(i*x)
print(max(palindromes))
