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