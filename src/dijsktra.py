from sys import argv
import re
# Infinity cost constant
INFINITY = 99999

file = open(argv[1], "r")
# The greatest node is equal to number of nodes - 1
greatest_node = -1
for line in file:
    # Reading only lines there are not comments
    if not re.match("//", line):
        info = line.split(" ")
        # Find the number of nodes
        if int(info[0]) > greatest_node:
            greatest_node = int(info[0])
        if int(info[1]) > greatest_node:
            greatest_node = int(info[1])            

file.close()

# Total number of nodes
nodes = greatest_node + 1
graph = []

# Open the file again
file = open(argv[1], "r")

# Constants for file manipulation
first_line = True
origin = 0
destiny = 0
for line in file:
    # Reading only lines there are not comments
    if not re.match("//", line):
        info = line.split(" ")
        if first_line:
            origin = int(info[0])
            destiny = int(info[1])
            first_line = False
        # Create JSON and remove \n of end of line
        else: 
            arrest = {info[0] + "&" + info[1]: info[2].replace('\n', '')}        
            # Add JSON to graph
            graph.append(arrest)
file.close()

# Constants for matrix approach
minimun = INFINITY
old_node = origin
current_node = origin
col = 1
matrix = [[INFINITY for x in range(nodes)] for y in range(nodes)]
cost = 0
for i in range(len(graph)):
    for node in range(len(graph)):
        n = list(graph[node].keys())[0].split("&")
        value = int(list(graph[node].values())[0])
        if int(n[0]) == current_node:
            # Check if the node is the origin, then set all columns as correspondent cost
            if int(n[0]) == origin:
                matrix[int(n[0])][int(n[0])] = 0
                matrix[int(n[0])][int(n[1])] = value
                # Check for the minimun distance and save the target node
                if value < minimun:
                    minimun = value
                    col = int(n[1])
            else:
                # If isn't the origin node, then look back to see if the current cost is smaller than the previous
                print("--- ",n[0], n[1], matrix[int(n[0]) - 1][int(n[1])], value)
                if matrix[old_node][int(n[1])] < value:
                    # If it is, than keep the old cost
                    matrix[int(n[0])][int(n[1])] = matrix[old_node][int(n[1])]
                    if matrix[int(n[0])][int(n[1])] < minimun:
                        minimun = matrix[int(n[0])][int(n[1])]
                        col = int(n[1])
                else:
                    # If isn't, than set the new cost using the actual cost to current node
                     matrix[int(n[0])][int(n[1])] = cost + value 
                     if matrix[int(n[0])][int(n[1])] < minimun:
                        minimun = matrix[int(n[0])][int(n[1])]  
                        col = int(n[1])
    # Set new current node
    old_node = current_node
    current_node = col
    cost = minimun
    if current_node == destiny:
        break;
    minimun = INFINITY

print(matrix)
print("-- Minimun Cost --")
print(cost)