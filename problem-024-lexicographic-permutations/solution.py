from itertools import permutations

perms = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
possible_perm = 3628800
lalala = []
x = 1


for i in perms:
    lalala.append(i)
    x +=1
    if x > 1000000:
        break


print(lalala[999999])


import math
#find permutation with index 999999; the permutation with index 0 is:
first_permutation = [0, 1, 2, 3, 4, 5, 6, 7 , 8 ,9]
my_permutation = []
# lets write 999999 = 2 * 9! + 274239:
number_to_find = 999999
for i in range(9, -1, -1):
    multiplier = number_to_find // math.factorial(i)
    number_to_find = number_to_find % math.factorial(i)
    my_permutation.append(first_permutation[multiplier])
    first_permutation.pop(multiplier)
    
    


print(my_permutation)


number_to_find = 999999
print(number_to_find % math.factorial(9))
print(number_to_find // math.factorial(9))
