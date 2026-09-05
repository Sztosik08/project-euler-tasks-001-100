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
    
# We have the pattern so now we have a 1001 by 1001 spiral. For 9x9 we need to generate 4 grids (not counting the 1x1) so for 1001x1001 grid we need (1001-1)/2 grids so 500
    

grids_28 = []
step = 2
last_nr_in_seq = 1
total_28 = 1
for i in range (1, 501):
    grids_28.append([last_nr_in_seq+step, last_nr_in_seq+step*2, last_nr_in_seq+step*3, last_nr_in_seq+step*4])
    total_28 += sum(grids_28[-1])
    step += 2
    last_nr_in_seq = grids_28[-1][-1]
    
print(total_28)
