# 백준 2887 행성 터널
def find(k):
    while numbers[k] != k:
        k = numbers[k]
    return k

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        numbers[y] = x
    else:
        numbers[x] = y


N = int(input())
numbers = [i for i in range(N)]
xyz = [[] for _ in range(3)]
connections = []
ans = 0
for i in range(N):
    a, b, c = map(int, input().split())
    xyz[0].append([i, a])
    xyz[1].append([i, b])
    xyz[2].append([i, c])

for i in range(3):
    xyz[i].sort(key=lambda x: x[1])

for i in range(3):
    for j in range(N-1):
        connections.append([xyz[i][j][0], xyz[i][j+1][0], abs(xyz[i][j][1] - xyz[i][j+1][1])])

connections.sort(key=lambda x: x[2])

for i in range(len(connections)):
    if find(numbers[connections[i][0]]) != find(numbers[connections[i][1]]):
        union(connections[i][0], connections[i][1])
        ans += connections[i][2]

print(ans)