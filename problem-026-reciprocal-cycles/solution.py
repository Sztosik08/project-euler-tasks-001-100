# sequence in a fraction

def fractionToDecimal(numr, denr):

    res = ""
    mp = {}

    # Find first remainder
    rem = numr % denr
    # Keep finding remainder until either
    # remainder becomes 0 or repeats
    while ((rem != 0) and (rem not in mp)):

        # Store this remainder
        mp[rem] = len(res)

        # Multiply remainder with 10
        rem = rem * 10

        # Append rem / denr to result
        res_part = rem // denr
        res += str(res_part)
        # Update remainder
        rem = rem % denr

    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]


sequences_26 = []
for i in range(1, 1000):
    sequences_26.append(fractionToDecimal(1, i))


longest_recurr = max(sequences_26, key=len)
print(sequences_26.index(longest_recurr)+1)
