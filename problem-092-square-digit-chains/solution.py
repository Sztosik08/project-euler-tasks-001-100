sum_digs_to_1 = set()
sum_digs_to_89 = set()

to_89 = 0

for i in range(1, 10000000):
    first = add_sq(i)
    if first in sum_digs_to_89:
        to_89 +=1
        continue
    if first in sum_digs_to_1:
        continue
    chain = [i]
    nr = 0
    while True:
        
        nr = add_sq(chain[-1])
        if nr == 89:
            to_89 += 1
            for item in chain:
                sum_digs_to_89.add(item)
            break
        if nr == 1:
            for item in chain:
                sum_digs_to_1.add(item)
            break
        if nr != chain[-1]:
            chain.append(nr)
            
print(to_89)
