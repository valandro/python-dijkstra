from sys import argv
import re

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

# nodes = number max of nodes
nodes = greatest_node + 1
file.close()
graph = []
file = open(argv[1], "r")
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
minimun = INFINITY
current_node = origin
col = 0
matrix = [[INFINITY for x in range(nodes)] for y in range(nodes)]

for i in range(len(graph)):
    for node in range(len(graph)):
        n = list(graph[node].keys())[0].split("&")
        if int(n[0]) == current_node: 
            if current_node == origin:
                matrix[origin][origin] = 0
            matrix[int(n[0])][int(n[1])] = int(list(graph[node].values())[0])
            if int(list(graph[node].values())[0]) < minimun:
                minimun = int(list(graph[node].values())[0])
                col = int(n[1])
                print(minimun, col)

    current_node = i + 1
    print(current_node)
print(matrix)
