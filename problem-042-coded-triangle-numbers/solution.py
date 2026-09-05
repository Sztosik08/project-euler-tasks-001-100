char_codex = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,
              'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 
              'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 
              's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24,
              'y':25, 'z':26}

def calculate_alphabetic_score(name):
    name = list(name.lower())
    alphabetic_score = 0
    for char in name:
        alphabetic_score += char_codex[char]
    return alphabetic_score

def triangle_number(n):
    return int(1/2*n*(n+1))


f = open("0042_words.txt")
content = f.read()
raw_content = content.split(",")
import re
words = []
for element in raw_content:
    name = re.sub(r'[^a-zA-Z0-9]', '', element)
    words.append(name)
words.sort()

triangle_nrs = []
for i in range(1, 40):
    triangle_nrs.append(triangle_number(i))


count = 0
for word in words:
    if calculate_alphabetic_score(word) in triangle_nrs:
        count += 1
print(count)
