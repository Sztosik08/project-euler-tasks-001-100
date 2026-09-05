#brute force
dist_list = []
for a in range(2,101):
    for b in range(2,101):
        nr = a**b
        if nr not in dist_list:
            dist_list.append(nr)
            
print(len(dist_list))


# but using a set() function we can do it like that:
print(len(set(a**b for a in range(2,101) for b in range(2,101))))
