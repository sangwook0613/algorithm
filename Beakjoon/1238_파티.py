def dijkstra(start):
    visited = [0]*(N+1)
    weight = [0] + [987654321]*N
    visited[start] = 1
    if start != X:
        weight[start] = 0

    for n, w in nodes[start]:
        weight[n] = w

    for _ in range(1, N):
        # print([weight[i] for i in range(1, N+1) if not visited[i]])
        min_idx = weight.index(min([weight[i] for i in range(1, N+1) if not visited[i]]))
        # print(min_idx)
        visited[min_idx] = 1
        for n, w in nodes[min_idx]:
            weight[n] = min(weight[n], weight[min_idx] + w)

    return weight


N, M, X = map(int, input().split())

nodes = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    chk = 0
    for w in range(len(nodes[start])):
        if nodes[start][w][0] == end:
            nodes[start][w][1] = min(nodes[start][w][1], weight)
            chk = 1
            break
    if chk:
        continue
    nodes[start].append([end, weight])

result = dijkstra(X)
for k in range(1, N+1):
    temp = dijkstra(k)
    result[k] += temp[X]

print(max(result))