CUBES = [1, 4, 9, 16, 25, 36, 49, 64, 81]

import itertools

my_combinations = []

for c in itertools.combinations(range(10),6):
    if set(c) not in my_combinations:
        my_combinations.append(set(c))
        
for comb in my_combinations:
    if 6 in comb and 9 not in comb:
        comb.add(9)
    elif 9 in comb and 6 not in comb:
        comb.add(6)

def is_valid_comb(c1, c2):
    to_check = []
    for a in c1:
        for b in c2:
            to_check.append(a*10+b)
            to_check.append(b*10+a)
            
    to_check = set(to_check)
    
    for item in CUBES:
        if item not in to_check:
            return(False)
        
    return(True)
            
count = 0
for i in range(0, len(my_combinations)-1):
    for j in range(i+1, len(my_combinations)):
        if is_valid_comb(my_combinations[i],my_combinations[j]):
            count +=1

print(count)
