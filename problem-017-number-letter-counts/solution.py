# words_i_need = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
#                "seventeen", "eighteen", "nineteen", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]

number_to_word = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}

def letter_counter(n, dict_n):
    word = []
    digits_17 = list(map(int, str(n)))
    if len(digits_17) == 4:
        word.append("onethousand")
        return word
    if len(digits_17) == 3:
        word.append(dict_n[digits_17[0]])
        word.append("hundred")
        if digits_17[1] == 0 and digits_17[2] == 0:
            pass
        else:
            word.append("and")
        if digits_17[1] == 1:
            word.append(dict_n[digits_17[2]+10])
        else:        
            word.append(dict_n[digits_17[1]*10])
            word.append(dict_n[digits_17[2]])
        return word
    if len(digits_17) == 2:
        if digits_17[0] == 1:
            word.append(dict_n[digits_17[1]+10])
        else:
            word.append(dict_n[digits_17[0]*10])
            word.append(dict_n[digits_17[1]])
        return word    
    if len(digits_17) == 1:
        word.append(dict_n[digits_17[0]])
        return word


sum_17 = 0
for i in range(1,1001):
    word_17 = ''.join(letter_counter(i, number_to_word))
    sum_17 += len(word_17)

print(sum_17)
