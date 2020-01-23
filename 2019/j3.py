# CCC 2019 J3 - Cold Compress

# take input for number of lines
N = int(input())

# Create list to hold the decoded inputs
lines = [None]*N

# Take line inputs
for i in range(N):
    lines[i] = input()

# Function to encode a line
def encode(line):
    output = ''             # Empty output string
    lastChar = line[0]      # Start comparing to the first character
    count = 0               # The quantity of the current character is 0
    for c in line:
        if c == lastChar:   # If the current character is the same as the last, increment counter
            count += 1
        else:
            # If the current character is different than the last,
            # add the quantity and previous character to the output,
            # and reset the counter to 1 (not 0, because the new character has occurred)
            output += str(count) + " " + lastChar + " "
            count = 1
            
            lastChar = c
    
    output += str(count) + " " + lastChar + " "     # Add to the output again, as the last character would not have been processed yet
    return output[:-1]                              # Remove the extra space at the end of the output before returning

# Print oupput
for n in lines:
    print(encode(n))
    
    
