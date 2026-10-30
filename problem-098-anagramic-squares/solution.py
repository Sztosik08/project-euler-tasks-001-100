f = open("problem-098-anagramic-squares/words.txt")
content = f.read().strip()
raw_content = content.split(',')
raw_content = [element.replace('"', '') for element in raw_content]


# let's write a helper function to obtain all eligble word pairs

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
    
word_pairs = []

for i in range(len(raw_content)-1):
    for j in range(i+1, len(raw_content)):
        if is_anagram(raw_content[i], raw_content[j]):
            word_pairs.append([raw_content[i], raw_content[j]])
            
# now that we got word pairs let's create a dictionary of 2, 3, 4 etc digit squares
# let's find the length of the longest word/words

longest = 0
word = []
for pair in word_pairs:
    if len(pair[0]) > longest:
        longest = len(pair[0])
        word = pair
        
# print(longest) The longest word is 9 digit so we create a dictionary with a max key of 9 digits

squares = {}

for n in range(1, int((10**9)**0.5)):
    sq = n**2
    length = len(str(sq))
    if length not in squares:
        squares[length] = []
    squares[length].append(sq)
    
#now a mapping function word words in word_pairs to square 

def map_word(word, square):
    s = str(square)
    d = {}
    for letter, digit in zip(word, s):
        if letter in d:
            if d[letter] != digit:
                return None
        else:
            d[letter] = digit
    if len(set(d.values())) != len(d):
        return None
    return d



best = 0

for w1, w2 in word_pairs:
    for sq in squares[len(w1)]:
        mapping = map_word(w1, sq)
        if mapping is None:
            continue
        number_str = "".join(str(mapping[letter]) for letter in w2)
        if number_str[0] == "0":
            continue
        result = int(number_str)
        if result in squares[len(w2)]:
            if result > best:
                best = result
            if sq > best:
                best = sq
                
print(f"the solution is: {best}")