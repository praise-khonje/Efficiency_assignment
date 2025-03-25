x = [3, 1, 5, 2, 4]
target = 9

seen = set()
printed = set()

for num in x:
    complement = target - num
    pair = (min(num, complement), max(num, complement))
    if complement in seen and pair not in printed:
        print(f"Pair found: {pair[0]} + {pair[1]} = {target}")
        printed.add(pair)
    seen.add(num)
