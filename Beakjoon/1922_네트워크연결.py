def find(a):
    if a != computers[a]:
        computers[a] = find(computers[a])
    return computers[a]

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        computers[x] = y
    else:
        computers[y] = x


N = int(input())
M = int(input())
computers = [i for i in range(N+1)]
connections = []

for _ in range(M):
    connections.append(list(map(int, input().split())))

connections.sort(key=lambda a:a[2])

ans = 0
for i in range(M):
    if find(connections[i][0]) != find(connections[i][1]):
        union(connections[i][0], connections[i][1])
        ans += connections[i][2]

print(ans)