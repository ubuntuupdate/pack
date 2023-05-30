def coloring(graph, v):
    result = [-1] * v
    result[0] = 0

    available = [False] * v

    for u in range(1, v):
        for i in graph[u]:
            if(result[i] != -1):
                available[result[i]] = True

        cr = 0
        while cr < v:
            if (available[cr] == False):
                break

            cr += 1

        result[u] = cr

        for i in graph[u]:
            if (result[i] != -1):
                available[result[i]] = False

    for u in range(v):
        print('vertex', u, '--> color', result[u])


graph = [[0, 1, 1, 0, 0],
         [1, 0, 1, 1, 0],
         [1, 1, 0, 1, 0],
         [0, 1, 1, 0, 1],
         [0, 0, 0, 1, 0]]

coloring(graph, 5)