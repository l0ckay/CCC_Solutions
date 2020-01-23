# CCC 2019 J5 - Rule of Three
# This solution uses a tree structure to generate the path to the solution
# using some optimization to reduce repeated calculations

# Not tested with the Online Grader. It works quickly with all of the test data

import re

# Create a Node class to make a tree
class Node():
    def __init__(self, parent, data): # Constructor
        
        self.data = data
        
        if parent == 'root':
            # If 'root' is passed as the parent, then the depth of the node is 0
            self.isRoot = True
            self.depth = 0
        else:
            self.parent = parent
            self.isRoot = False
            self.depth = parent.depth + 1   # Depth is 1 more than the depth of the parent
            parent.addChild(self)           # Add the new node to its parent's children list
            self.setRule(-1, -1)            # Add in placeholder values

        self.children = []

    def setRule(self, ruleNum, position):
        # Save the rule number and position than created this node from its parent
        self.ruleNum = ruleNum
        self.rulePosition = position

    def __str__(self):
        # Override the default str function
        return " ".join([str(self.ruleNum), str(self.rulePosition), self.data])

    def addChild(self, child):
        # Add a node to the children list
        self.children.append(child)

    def path(self):
        # Return the series of rule substitutions that leads to this node
        # Does not include the root
        output= ''
        curNode = self
        while not curNode.isRoot:
            output = str(curNode) + "\n" + output   # Add in the current node
            curNode = curNode.parent                # Move to the current node's parent
        return output[:-1] # Remove the last line break

# INPUT

# List of length 3 for the substitution rules
fromSubs = ['']*3
toSubs = ['']*3

for i in range(3):
    # Take the 3 lines of input for the rules
    fromSubs[i], toSubs[i] = input().split(" ")

# Take input for the last line
steps, startString, endString = input().split(" ")
steps = int(steps) # Convert steps to an integer

# Create root node that starts on the starting string
root = Node('root', startString)

# Keep list holding the rows of the tree for easy access
treeNodes = [[root]]
for i in range(steps):
    # Add rows to the treeNodes list
    treeNodes.append([])

def startingPositions(line, key):
    # Return all of the positions that a key starts at in a string
    # The "(?=(...))" in finditer allows overlapping positions to both be recognized
    return [match.start() for match in re.finditer("(?=("+key+"))", line)]

# Create the tree
def makeTree():
    global treeNodes, fromSubs, toSubs, steps, endString
    for row in treeNodes:
        for node in row:
            for rule in range(3): # Iterate through each rule
                startPos = startingPositions(node.data, fromSubs[rule]) # find the starting positions of the current rule
                for pos in startPos:
                    newData = node.data[:pos]+toSubs[rule]+node.data[pos+len(fromSubs[rule]):]  # form the subsituted string
                    if not newData in [d.data for d in treeNodes[node.depth+1]]:                # If the data is new to the row of the tree, create a child
                        child = Node(node, newData)
                        child.setRule(rule+1, pos+1)
                        treeNodes[child.depth].append(child)
                        if newData == endString and child.depth == steps:
                            # If the new child is the output, and the depth matches the required number of steps
                            # Print the path to the child and return to exit
                            print(child.path())
                            return

makeTree()
                
