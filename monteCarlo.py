import random
import math

def generateArray(n):
    array = [0 if random.random()-0.5 < 0 else 1 for x in range(n)]
    return array

def main(n, k):
    a = generateArray(n)

    j, tries = 0, 0
    while j < k:
        tries += 1
        i = math.floor(random.random() * n)
        if a[i] == 1:
            return f"The first 1 is found at index {i} in {tries} tries."
        j += 1
    return f"Couldn't find a 1 after {j} attempts."
        
# ================================================
print(main(10000, 2))