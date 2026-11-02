import operator


ops = [operator.add, operator.sub, operator.mul, operator.truediv]

possible_sequences = []

for a in range(0, 7):
    for b in range(a+1, 8):
        for c in range(b+1, 9):
            for d in range(c+1, 10):
                possible_sequences.append([a,b,c,d])

def get_consecutive_sequence(numbers):
    if not numbers:
        return []
    
    result = []

    expected = 1 
    
    for num in numbers:
        if num == expected:
            result.append(num)
            expected += 1
        else:

            break
            
    return result

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def reachable(nums):
    if len(nums) == 1:
        return {nums[0]}
    results = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
            for op in ops:
                if op is operator.truediv and nums[j] == 0:
                    continue
                results |= reachable(rest + [op(nums[i], nums[j])])
    
    ordered_list = []            
    for item in results:

        if item>0 and is_integer_num(item):
            ordered_list.append(item)

            
    return set(ordered_list)


longest, sequence = 0, []

for seq in possible_sequences:
    curr_sequence = reachable(seq)
    cons_sequence = get_consecutive_sequence(curr_sequence)
    
    if len(cons_sequence) > longest:
        longest, sequence = len(cons_sequence), seq
    

# print(get_consecutive_sequence(reachable(nums)))
print(f" the longest sequence is: {longest} numbers. And the answer to the question is the {sequence}")

answer = ""
for item in sequence:
    answer += str(item)

print(f" so the answer is: {answer}")
