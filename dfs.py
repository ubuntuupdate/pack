graph={
    '5':['3','7'],
    '3':['2','4', '5'],
    '7':['5', '8'],
    '2':['3'],
    '4':['3', '8'],
    '8':['4', '7']
}

def dfs(graph, node):
    stack = []
    visited = []
    if node not in visited:
        visited.append(node)
        print(node, end=' ')
        for neighbour in graph[node]:
            stack.append(neighbour)
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            print(n, end=' ')
            for neighbour in graph[n]:
                stack.append(neighbour)

dfs(graph, '5')