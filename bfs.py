graph={
    '5':['3','7'],
    '3':['2','4', '5'],
    '7':['5', '8'],
    '2':['3'],
    '4':['3', '8'],
    '8':['4', '7']
}

def bfs(graph, node):
    visited = []
    queue = []

    if node not in visited:
        visited.append(node)
        print(node, end=' ')
        for neighbour in graph[node]:
            queue.append(neighbour)

    while queue:
        n = queue.pop(0)

        if n not in visited:
            visited.append(n)
            print(n, end=' ')
            for neighbour in graph[n]:
                queue.append(neighbour)

bfs(graph, '5')