# CCC 2019 J1 - Winning Score

# Variables for scores of Apples and Bananas
apples = 0
bananas = 0

# Calculate score for apples
for a in range(3, 0, -1): # a = 3, 2, 1 --> score multiplier
    # Add the line input times the score multiplier to the score
    apples += a * int(input())

# Calculate score for bananas
for b in range(3, 0, -1):
    bananas += b * int(input())

# Print winner
if apples > bananas:
    print("A")
elif bananas > apples:
    print("B")
else:
    print("T")
    
