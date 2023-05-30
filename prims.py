
def prims(graph, starting_node=0):
    INF = 9999

    vertices = len(graph[0])

    selected = [False] * vertices

    edges = 0

    selected[starting_node] = True

    sum = 0

    while edges < vertices-1:
        min = INF
        x = 0
        y = 0

        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if (not selected[j]) and graph[i][j]:
                        if min > graph[i][j]:
                            min = graph[i][j]
                            x = i
                            y = j

        print(str(x) + '-' + str(y) + ' : ' + str(graph[x][y]))
        selected[y] = True
        edges += 1
        sum += graph[x][y]

    print('Total weight: ', sum)


graph = [[0, 4, 4, 0, 0, 0],
         [4, 0, 2, 0, 0, 0],
         [4, 2, 0, 3, 2, 4],
         [0, 0, 3, 0, 0, 3],
         [0, 0, 2, 0, 0, 3],
         [0, 0, 4, 3, 3, 0]]

prims(graph, 4)
