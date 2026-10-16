f = open("problem-089-roman-numerals/roman.txt")
content = f.read()
raw_content = content.split()

rom_symbols = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

int_symbols = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

def rom_to_int(n):
    
    ints = [rom_symbols[c] for c in n]
  
    total = 0
    
    for i in range(len(ints)-1):
        if ints[i+1] > ints[i]:
            total -= ints[i]
        else:
            total += ints[i]
    
    total += ints[-1]
    
    return(total)

def int_to_rom(n):
    rom = ""
    for k in int_symbols:
        while n >= k:
            rom += int_symbols[k]
            n -= k
            
    return rom

roman = []

for el in raw_content:
    integer = (rom_to_int(el))
    roman.append(int_to_rom(integer))
    
total_raw = 0
total_processed = 0

for el in raw_content:
    total_raw += len(el)
for el in roman:
    total_processed += len(el)
    
    
print(f"total_raw: {total_raw}, total_processed: {total_processed}, answer: {total_raw-total_processed}")
