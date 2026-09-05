# --- Attempt 1 ---
def ispandigital(string):
    if len(string) != 9:
        return False
    
    ch = "".join(sorted(string))
    
    if (ch == "123456789"):
        return True
    else:
        return False

def Pandigital_Product_1_9(n): 
    
    i = 1
    while i * i <= n:
        
        if ((n % i == 0) and
             ispandigital(str(n) + str(i) + str(n // i))) == True:
            return True
            
        i += 1
    
    return False


feasable_products = []

for i in range(1, 98766):
    if Pandigital_Product_1_9(i) == True:
        feasable_products.append(i)
    
    


# --- Attempt 2 ---
print(feasable_products)
print(sum(feasable_products))
