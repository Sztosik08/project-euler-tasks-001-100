# --- Attempt 1 ---
#check for the upper bound

import matplotlib.pyplot as plt
def f(x):
    return sum(int(c)**5 for c in str(x))
x = range(0, 1500001)
y = [f(i) for i in x]
plt.figure(figsize=(12, 6))
plt.plot(x, y, linewidth=0.5)
plt.xlabel("X")
plt.grid(True)

plt.show()


# --- Attempt 2 ---
# from the chart we see that it won't be higher than 6*9**5 = 354294 though I cannot be 100% sure 


# --- Attempt 3 ---
#brute force 
ns_of_5th = []
for i in range(2,354295):
    cur_sum = f(i)
    if cur_sum == i:
        ns_of_5th.append(i) 
    


# --- Attempt 4 ---
print(ns_of_5th)
print(sum(ns_of_5th))
