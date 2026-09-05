# --- Attempt 1 ---
import math
def n3(n):
    return (n*(n+1))//2
def n4(n):
    return n**2
def n5(n):
    return (n*(3*n-1))//2
def n6(n):
    return (n*(2*n-1))
def n7(n):
    return (n*(5*n-3))//2
def n8(n):
    return (n*(3*n-2))

def is_set(a, b):
    if len(str(a)) != 4 or len(str(b)) != 4:
        return False
    return str(a)[2:] == str(b)[:2]


# --- Attempt 2 ---
functs = [n3, n4, n5, n6, n7, n8]
viable_nr = []


for fun in functs:
    current = []
    n = 1
    while len(str(fun(n))) < 4:
        n+=1
    while len(str(fun(n))) == 4:
        current.append(fun(n))
        n+=1  
    viable_nr.append(current)
    


# --- Attempt 3 ---
# solution 1

from itertools import permutations
perm = permutations([0,1,2,3,4,5])

curr_it = []


for p in perm:
    for nr in viable_nr[p[0]]:
        curr_it = []
        curr_it.append(nr)
        for nr2 in viable_nr[p[1]]:
            if is_set(nr, nr2):
                curr_it.append(nr2)
                for nr3 in viable_nr[p[2]]:
                    if is_set(nr2, nr3):
                        curr_it.append(nr3)
                        for nr4 in viable_nr[p[3]]:
                            if is_set(nr3, nr4):
                                curr_it.append(nr4)
                                for nr5 in viable_nr[p[4]]:
                                    if is_set(nr4, nr5):
                                        curr_it.append(nr5)
                                        for nr6 in viable_nr[p[5]]:
                                            if is_set(nr5, nr6) and is_set(nr6, nr):
                                                curr_it.append(nr6)
                                                print(curr_it, sum(curr_it))
                                                break


# --- Attempt 4 ---
# solution 2

def build_chain(chain, remaining_sets):
    if len(remaining_sets) == 0:
        if is_set(chain[-1], chain[0]):
            return chain
        return None
    
    current_end = chain[-1]
    next_set = viable_nr[remaining_sets[0]]
    
    for candidate in next_set:
        if is_set(current_end, candidate):
            result = build_chain(chain + [candidate], remaining_sets[1:])
            if result:
                return result
    return None

for perm in permutations([0,1,2,3,4,5]):
    for start in viable_nr[perm[0]]:
        result = build_chain([start], list(perm[1:]))
        if result:
            print(sum(result))
