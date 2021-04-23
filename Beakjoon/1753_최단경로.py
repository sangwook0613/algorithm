import heapq
INF = int(1e9)


def dij(start):
    weight = [0] + [INF]*V
    weight[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, idx = heapq.heappop(q)
        if weight[idx] < cost:
            continue
        for i, d in nodes[idx]:
            temp = cost + d
            if temp < weight[i]:
                weight[i] = temp
                heapq.heappush(q, (temp, i))

    return weight


V, E = map(int, input().split())
K = int(input())
nodes = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, w = map(int, input().split())
    nodes[start].append((end, w))

ans = dij(K)
for i in range(1, V+1):
    if ans[i] == INF:
        print('INF')
        continue
    print(ans[i])