def dijkstra(start):
    visited[start] = 1
    weight[start] = 0
    for node in nodes[start]:
        weight[node[0]] = node[1]

    cnt = 1
    while cnt <= N+1:
        min_idx = [0, 111111*N]
        for i in range(1, N+1):
            if not visited[i]:
                if weight[i] < min_idx[1]:
                    min_idx[0] = i
                    min_idx[1] = weight[i]
        visited[min_idx[0]] = 1
        cnt += 1
        for node in nodes[min_idx[0]]:
            weight[node[0]] = min(weight[node[0]], weight[min_idx[0]] + node[1])


N = int(input())
M = int(input())

nodes = [[] for _ in range(N+1)]
weight = [111111]*(N+1)
for _ in range(M):
    start, end, w = map(int, input().split())
    nodes[start].append([end, w])

visited = [0]*(N+1)
a, b = map(int, input().split())
dijkstra(a)
print(weight[b])
