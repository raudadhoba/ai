graph = {
    'A': ['B', 'E', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B','E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

# Visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # Keep track of all visited nodes
    explored = []
    # Keep track of nodes to be checked
    queue = [start]

    # Keep looping until there are nodes still to be checked
    while queue:
        # Pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # Add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # Add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)

    return explored

print(bfs_connected_component(graph, 'A'))
