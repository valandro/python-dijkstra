![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

# Dijsktra Algorithm

`Dijkstra's algorithm` is an algorithm for finding `the shortest paths between nodes in a graph`, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

### Running

```
python src/prim.py examples/graph1.wug
```

### Weighted Directed Graph
Examples:

**Graph 1**

![Graph image](/img/graph1.png)

**graph1.wdg**

```
(origin) (destiny)
1 5
(node) (node) (distance)
1 2 7
1 6 14
1 3 9
2 3 10
2 4 15
3 4 11
3 6 2
4 5 6
6 5 5
```

**Graph 2**

![Graph image](/img/graph2.png)

**graph2.wdg**

```
(origin) (destiny)
1 6
(node) (node) (distance)
1 2 5
1 3 2
2 4 4
2 5 2
3 2 8
3 5 7
4 6 3
4 5 6
5 6 1
```


### License
MIT License. [Click here for more information.](LICENSE)