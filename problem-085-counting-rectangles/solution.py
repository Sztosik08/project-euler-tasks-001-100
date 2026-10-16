# counting rectangles

w = 3 #width (columns)
h = 2 #height (rows)

# general formula: (h*(h+1))/2 * (w*(w+1))/2

def count_rectangles(h, w):
    return (h*(h+1))//2 * (w*(w+1))//2, w*h #number of rectangles, area

best_diff = float('inf')
best_area = 0

for h in range(1, 101):
    for w in range(1, 101):
        count = count_rectangles(h, w)[0]
        diff = abs(count - 2_000_000)
        if diff < best_diff:
            best_diff = diff
            best_area = h * w
            height = h
            width = w

print(best_area, best_diff)
print(height, width)
print("\n")
print(f"The answer is: {best_area}")
