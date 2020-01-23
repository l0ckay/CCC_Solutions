# CCC 2019 J2 - Time to Decompress

lines = int(input())

# List for quantity and characters
quantity = [None]*lines
chars = [None]*lines

# Take input for encoded message
for i in range(lines):
    quantity[i], chars[i] = input().split(" ")

# Print the output
for i in range(lines):
    print(chars[i] * int(quantity[i])) # Quantity is still a string, so convert to integer
