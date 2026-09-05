# --- Attempt 1 ---
def gen_collatz_seq(n):
    sequence = [n]
    curr_n = n
    while curr_n > 1:
        if curr_n % 2 == 0:
            curr_n *= 1/2
        else:
            curr_n = curr_n * 3 + 1
        sequence.append(int(curr_n))
    return sequence


sequences = []
for i in range(1,1000000):
    i_th_seq = gen_collatz_seq(i)
    sequences.append(i_th_seq)


# --- Attempt 2 ---
len_seq = []
for i in range(len(sequences)):
    len_seq.append(len(sequences[i]))

answer_14 = len_seq.index(max(len_seq)) + 1
print(answer_14)
