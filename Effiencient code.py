x = [3, 1, 5, 2, 4]
target = 4

# Linear search
if target in x:
    index = x.index(target)
    print(f"Found at index {index}")
else:
    print("Not found")
