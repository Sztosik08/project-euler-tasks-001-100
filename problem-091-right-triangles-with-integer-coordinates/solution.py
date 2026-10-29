import itertools 

#helpers 
def lenght_sq(cords1, cords2):
    return ((cords2[0]-cords1[0])**2 + (cords2[1]-cords1[1])**2)

def is_right_triangle(coords):
    lengths = []
    for comb in itertools.combinations(coords, 2):
        lengths.append(lenght_sq(comb[0], comb[1]))

    a, b, c = sorted(lengths)
    return a + b == c


#solution
grid_size = 50

all_points = [item for item in itertools.product(range(grid_size+1), repeat=2)]
all_points.remove((0,0))

    
count = 0

for p, q in itertools.combinations(all_points, 2):
    if is_right_triangle((p, q, (0, 0))):
        count += 1
        
print(f"the answer is: {count}")
