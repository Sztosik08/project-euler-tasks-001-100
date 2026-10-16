# board setup
import numpy as np


board = ["GO",
         "A1",
         "CC1",
         "A2",
         "T1",
         "R1",
         "B1",
         "CH1",
         "B2",
         "B3",
         "JAIL",
         "C1",
         "U1",
         "C2",
         "C3",
         "R2",
         "D1",
         "CC2",
         "D2",
         "D3",
         "FP",
         "E1",
         "CH2",
         "E2",
         "E3",
         "R3",
         "F1",
         "F2",
         "U2",
         "F3",
         "G2J",
         "G1",
         "G2",
         "CC3",
          "G3",
          "R4",
          "CH3",
          "H1",
          "T2",
          "H2"]



special_squares = ["G2J", "CH1", "CH2", "CH3", "CC1", "CC2", "CC3"]
ordinary = [i for i, name in enumerate(board) if name not in special_squares]
special = [i for i, name in enumerate(board) if name in special_squares]

JAIL = board.index("JAIL") #30
G2J = board.index("G2J") #10
GO = board.index("GO") #0


# helpers 
def back_3(sq):
    target = (sq-3) % 40
    return landing_resolver(target)

def next_of(sq, prefix):
    i = (sq +1) % 40
    while not board[i].startswith(prefix):
        i = (i+1)%40
    return i

def add(result, dist, weight):
    for key, value in dist.items():
        result[key] = result.get(key, 0) + value * weight
    

def landing_resolver(sq_landed):
    if sq_landed in ordinary:
        return {sq_landed: 1.0}
    elif sq_landed == G2J: #G2J == 30 field automatically setting lander to "JAIL" == 10
        return {JAIL: 1.0}
    elif sq_landed in [2, 17, 33]: #Community Chest
        return {
            sq_landed: 14/16,
            JAIL: 1/16,
            GO: 1/16
        }
    elif sq_landed in [7, 22, 36]: #Chance
        result = {}
        add(result, {sq_landed: 1.0}, 6/16)
        
        #fixed destination
        for target in [5, 11, 24, 39]:
            add(result, {target: 1.0}, 1/16)
        
        # next R or next U
        add(result, {next_of(sq_landed, "R"): 1.0}, 2/16)
        add(result, {next_of(sq_landed, "U"): 1.0}, 1/16)
        
        #back_3
        add(result, back_3(sq_landed), 1/16)
        
        add(result, {GO: 1.0}, 1/16)
        add(result, {JAIL: 1.0}, 1/16)
        
        return result
            
  
# dices
import itertools

nr_dices = 2
sides = 4
combs = list(itertools.product(range(1, sides + 1), repeat=nr_dices)) 

# build a matrix 120x120 (40 squares with a double count of 0,1,2 so 3x40)

n_sq = len(board) # 40
n_states = n_sq * 3

def idx(sq, d):
    return sq * 3 + d

rolls = []

for comb in combs:
    n = []
    n.append(comb[0] + comb[1])
    
    n.append(comb[0] == comb[1])

    n.append(1/len(combs))
    rolls.append(n)
    
M = np.zeros((n_states, n_states))

for sq in range(n_sq):
    for d in range(3):
        row = idx(sq,d)
        
        for total, is_double, p_roll in rolls:
            
            # 3rd double
            if is_double and d==2:
                M[row, idx(JAIL, 0)] += p_roll
                continue
            
            landed = (sq + total) % n_sq
            new_d = d+1 if is_double else 0
            
            for end_sq, p_end in landing_resolver(landed).items():
                if end_sq == JAIL:
                    M[row, idx(JAIL,0)] += p_roll*p_end
                else: 
                    M[row, idx(end_sq, new_d)] += p_roll * p_end     
                    
                    
v = np.zeros(n_states)
v[idx(0, 0)] = 1
for _ in range(1000):
    v = v @ M

dist = v.reshape(40, 3).sum(axis=1)
top3 = np.argsort(dist)[::-1][:3]


answ = ""
for i in top3:
    answ += str(i)
    
print(answ)