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

def main(n):
    """
    Summary: Generates an array of 1s and 0s and performs a Las Vegas-style search of the array for an occurrance of a 1

    Inputs:
        - n (int): Length of the array
    
    Outputs:
        - i (int): Index of the first 1 found
        - tries (int): Number of tries until a 1 was found
    """
    a = generateArray(n)

    tries = 0
    while True:
        tries += 1
        i = math.floor(random.random() * n)
        if a[i] == 1:
            return f"The first 1 is found at index {i} in {tries} tries."
        
# ================================================
print(main(10000))