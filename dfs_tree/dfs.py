def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)


# Define the graph as an adjacency list
graph = {
    0: [1],
    1: [2, 3],
    2: [1]
}

# Start DFS from node 0
visited = set()
dfs(graph, 0, visited)
