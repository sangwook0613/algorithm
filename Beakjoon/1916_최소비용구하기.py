BIG = int(1e9)

def dij(s, e):
    weight = [0] + [BIG]*N
    weight[s] = 0
    q = [(0, start)]

    while q:
        cost, idx = q.pop(0)
        if weight[idx] < cost:
            continue
        for i, w in node[idx]:
            temp = cost + w
            if temp < weight[i]:
                weight[i] = temp
                q.append((temp, i))

    return weight[e]


N = int(input())
M = int(input())
node = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    node[s].append((e, w))

start, end = map(int, input().split())
print(dij(start, end))