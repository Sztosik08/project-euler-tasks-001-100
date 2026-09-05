def tri(x):
    return (x*(x+1))//2

def pent(x):
    return (x*(3*x-1))//2

def hexa(x):
    return x*(2*x-1)
    


def is_tri_nr(n):
    x = (-1 + math.sqrt(8*n+1)) / 2
    return x == int(x)
    
def is_pent_nr(n):
    x = (1 + math.sqrt(1 + 24*n)) / 6
    return x == int(x)

def is_hex_nr(n):
    x = (1 + math.sqrt(8*n+1)) / 4
    return x == int(x)


print(hexa(143))


# i = 40755 is tri pent and 143th hex. We'll be checking only hex_nrs  
n = 144
i = hexa(n)

while is_tri_nr(i) == False or is_pent_nr(i) == False or is_hex_nr(i) == False:
    n +=1
    i = hexa(n)
    
print(i)

# because hex is always a tri nr and we're going through hex nrs we could simplify to:
 # while is_pent_nr(i) == False:
 # ..... 
 # but it's fine
