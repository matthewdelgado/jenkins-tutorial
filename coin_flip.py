import random

def coin_flip():
    # Generate a random number (0 or 1) to represent heads or tails
    result = random.randint(0, 1)
    
    if result == 0:
        return "Heads"
    else:
        return "Tails"

outcome = coin_flip()

print(outcome)
