# Sample graph implemented as a dictionary
graph = {
    'A': ['B', 'E', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

# Function to perform DFS
def dfs(graph, start):
    # Keep track of all visited nodes
    explored = []
    # Keep track of nodes to be checked
    stack = [start]
    
    # Keep looping until there are nodes still to be checked
    while stack:
        # Pop the last node from the stack
        node = stack.pop(-1)
        if node not in explored:
            # Add node to list of checked nodes
            explored.append(node)
            # Get neighbors of the node
            neighbours = graph[node]
            # Add neighbors of the node to the stack
            for neighbour in neighbours:
                stack.append(neighbour)
    
    return explored

# Test the DFS function
print(dfs(graph, 'A'))  # Expected output: ['A', 'C', 'G', 'F', 'E', 'D', 'B']