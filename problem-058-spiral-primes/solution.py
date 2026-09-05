# --- Attempt 1 ---
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False    
    return True

def get_prime_ratio(list_p): # not necessary at the end of the day
    count_p = 0
    for n in list_p:
        if isPrime(n):
            count_p +=1
    return count_p/len(list_p)


# --- Attempt 2 ---
# FROM PROBLEM 28 where we looked for the sum of the numners on the diagonals we got :


    # 5 by 5 is 25 numbers
    # 1001 by 1001 is 1002001 numbers

    # starting with 1 the 5 by 5 grid has 2 rings
    #   ring 1 is 3x3 (3, 5, 7, 9); ring 2 is 5x5 (13, 17, 21, 25)

    # while expanding the grid next one would be 7x7 (31, 37, 43, 49) and 9x9 (57, 65, 73, 81)

    # So the pattern we have here:
        # 1x1 is just 1 then:
        # 3x3 -> 4 numbers spaced by 2 -> 3, 5, 7, 9
        # 5x5 -> 4 numbers spaced by 2+2 and first is 9+2+2 -> 13, 17, 21, 25
        # 7x7 -> 4 numbers spaced by 4+2 and first is 25+4+2 -> 31, 37, 43, 49
        # 9x9 -> 4 numbers spaced by 4+2+2 and first is 49+4+2+2 -> 57, 65, 73, 81
        
    

diagonal_nr = [1]
step = 2
last_nr_in_seq = 1
grid_size = 1

prime_count = 0
total_count = 1
prime_ratio = 1.0

while prime_ratio > 0.10:
    for i in range(1,5):
        last_nr_in_seq += step
        if isPrime(last_nr_in_seq):
            prime_count +=1
   
    total_count += 4
    step += 2
    grid_size += 2

    prime_ratio = prime_count / total_count

    
# print(diagonal_nr)
print(prime_ratio)
print(grid_size)
