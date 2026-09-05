# --- Attempt 1 ---
def is_perm(a, b):
    if len(str(a)) != len(str(b)):
        return False
    return sorted(list(str(a))) == sorted(list(str(b)))


# --- Attempt 2 ---
cubes = []
for i in range(1, 30000):
    cubes.append(i**3)


# --- Attempt 3 ---
curr_it = []
for i in range(len(cubes)):
    curr_it = [cubes[i]]
    for j in range(i+1, len(cubes)):
        if is_perm(cubes[i], cubes[j]):
            curr_it.append(cubes[j])
            if len(curr_it) == 5:
                print(curr_it)
                break
    if len(curr_it) == 5:
        break
