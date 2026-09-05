# --- Attempt 1 ---
f = open("0059_cipher.txt")
content = f.read()
raw_content = content.split(',')
raw_content = list(map(int, raw_content))
print(raw_content)


# --- Attempt 2 ---
example = [36, 22, 80, 0, 0, 4]
key = [97, 98, 99]

for i, element in enumerate(example):
    print(chr(element^key[i % len(key)]))


# --- Attempt 3 ---
from itertools import product
import string

lowercase = [ord(c) for c in string.ascii_lowercase]
key_combinations = product(lowercase, repeat=3)


# --- Attempt 4 ---
for combination in key_combinations:
    decrypted = [chr(raw_content[i] ^ combination[i % 3]) for i in range(len(raw_content))]
    text = ''.join(decrypted)
    if 'the' in text and 'and' in text and 'of' in text and text.count(' ') > 200:  # detection condition
        print(sum(ord(c) for c in text))
        break


# --- Attempt 5 ---
print(text)
