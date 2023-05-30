graph = [[0, 4, 4, 0, 0, 0],
         [4, 0, 2, 0, 0, 0],
         [4, 2, 0, 3, 2, 4],
         [0, 0, 3, 0, 0, 3],
         [0, 0, 2, 0, 0, 3],
         [0, 0, 4, 3, 3, 0]]


def dijkstra(graph, starting_node=0):
    INF = 9999
    

    v = len(graph[0])
    distances = {n:INF for n in range(v)}

    distances[0] = 0

    for i in range(v):
        for j in range(v):
            if graph[i][j]:
                if distances[i]+graph[i][j] < distances[j]:
                    distances[j] = distances[i] + graph[i][j]

    print(distances)

dijkstra(graph)
