def check_divisions(n):
    divisors = [2,3,5,7,11,13,17]
    if len(n) != 10:
        return False
    else:
        for i in range(1,8):
            substring = int(''.join(n[i:i+3]))
            if substring % divisors[i-1] !=0:
                return False
        return True
        


from itertools import permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tups = list(permutations(digits, 10))

numbers = []
for number in tups:
    numbers.append(list(number))


answer_43 = []
for number in numbers:
    if check_divisions(number) == True:
        answer_43.append(int(''.join(map(str, number))))
    


print(sum(answer_43))
