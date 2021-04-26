# 크루스칼 알고리즘
def find(a):
    while a != node[a]:
        a = node[a]
    return a


def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        node[x] = y
    else:
        node[y] = x


V, E = map(int, input().split())
node = [i for i in range(V+1)]
connections = []

for _ in range(E):
    connections.append(list(map(int, input().split())))

connections.sort(key=lambda a: a[2])
ans = 0
for i in range(E):
    if find(connections[i][0]) != find(connections[i][1]):
        union(connections[i][0], connections[i][1])
        ans += connections[i][2]

print(ans)

# 프림 알고리즘
BIG = int(1e9)

def prim(start):
    weight = [BIG]*(V+1)
    visited = [0]*(V+1)
    weight[start] = 0

    for _ in range(V):
        idx = -1
        min_cost = BIG
        for k in range(1, V+1):
            if not visited[k] and weight[k] < min_cost:
                min_cost = weight[k]
                idx = k
        visited[idx] = 1
        for i, d in node[idx]:
            if not visited[i] and d < weight[i]:
                weight[i] = d

    return sum(weight[1:])


V, E = map(int, input().split())
node = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    node[s].append((e, w))
    node[e].append((s, w))

print(prim(1))