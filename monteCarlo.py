import random
import math

def generateArray(n):
    """
    Summary: Generates a random array of roughly the same number of 1s and 0s of length n

    Inputs:
        - n (int): Length of the array

    Outputs: A random array of roughly the same number of 1s and 0s of length n
    """
    array = [0 if random.random()-0.5 < 0 else 1 for x in range(n)]
    return array

def main(n, k):
    """
    Summary: Generates an array of 1s and 0s and performs a Monte Carlo-style search of the array for an occurrance of a 1

    Inputs:
        - n (int): Length of the array
        - k (int): Number of tries for Monte Carlo search
    
    Outputs:
        - i (int): Index of the first 1 found
        - tries (int): Number of tries until a 1 was found
        or
        - A statement saying that a 1 wasn't within k tries
    """
    a = generateArray(n)

    j, tries = 0, 0
    while j < k:
        tries += 1
        i = math.floor(random.random() * n)
        if a[i] == 1:
            return f"The first 1 is found at index {i} in {tries} tries."
        j += 1
    return f"Couldn't find a 1 after {k} attempts."
        
# ================================================
print(main(10000, 2))