import random

def flip_coin():
    # Generate a random number (0 or 1) to represent heads or tails
    result = random.randint(0, 1)
    
    # Use the result to determine the outcome
    if result == 0:
        return "Heads"
    else:
        return "Tails"

# Call the flip_coin function and print the result
outcome = flip_coin()
print("The coin landed on:", outcome)
