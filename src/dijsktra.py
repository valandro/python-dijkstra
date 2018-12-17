from sys import argv
import re

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
for line in file:
    # Reading only lines there are not comments
    if not re.match("//", line):
        info = line.split(" ")
        if first_line:
            origin = info[0]
            destiny = info[1]
            first_line = False
        # Create JSON and remove \n of end of line
        else: 
            arrest = {info[0] + "&" + info[1]: info[2].replace('\n', '')}        
            # Add JSON to graph
            graph.append(arrest)
file.close()


