from itertools import groupby

# Take the operation input (ex. "HVVHVHH")
operations = input()

positions = [1,2,3,4]
# UL = 1; UR = 2;
# BL = 3; BR = 4

# Create a list of the operations, grouped into consecutive operations
# Ex. operations = 'HHVHVVV' --> opsSep = ['HH','V','H','VVV']
opsSep = [''.join(group) for key,group in groupby(operations)]

# A new, simpler operation will be built
newOperation = ''

for opSegment in opsSep:
    # Iterate through all of the opsSep elements
    if len(opSegment) % 2 == 1:
        # If an operation is performed consecutively an even number of times, the effect is canceled
        # Similarly, an odd number of repeats is equivalent to just 1
        # Ex. 'HH' has no overall effect on the grid, as the second H undoes the first H
        # Ex. 'VVVVV' is equivalent to 'V'

        # Therefore, the simplified new operation is built by adding the flip character if the segment has an odd length
        newOperation += opSegment[0]

for x in newOperation:
    # Iterate through the new operation string and perform the necessary operation to modify the 'positions' list
    if x == "H":
        # 1 <-> 3
        # 2 <-> 4
        for p in range(len(positions)):
            positions[p] = (positions[p] + 1)%4+1 # This line converts 1 <-> 3 and 2 <-> 4, without needing any temporary storage values
    else:
        # 1 <-> 2
        # 3 <-> 4
        for p in range(len(positions)):
            positions[p] = positions[p] + 2 * (positions[p]%2) - 1 # Similar to above

# Output the numbers in positions 0 and 1  (UL and UR)
# Followed by the ones in positions 2 and 3 (BL and BR)
print(str(positions[0]),str(positions[1]))
print(str(positions[2]),str(positions[3]))
