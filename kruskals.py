def find(parent, node):
    if parent[node] == node:
        return node
    return find(parent, parent[node])

def union(parent, rank, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

def kruskal(graph):
    result = []

    edges = []
    for node in graph:
        for neighbor, weight in graph[node].items():
            edges.append((node, neighbor, weight))
    edges.sort(key=lambda edge: edge[2])

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    for edge in edges:
        node1, node2, weight = edge

        root1 = find(parent, node1)
        root2 = find(parent, node2)

        if root1 != root2:
            result.append(edge)
            union(parent, rank, root1, root2)

    return result

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

mst = kruskal(graph)
print("Minimum spanning tree:", mst)
