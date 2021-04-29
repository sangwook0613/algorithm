def find(a):
    if a != stars[a]:
        stars[a] = find(stars[a])
    return stars[a]

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        stars[x] = y
    else:
        stars[y] = x


N = int(input())
stars = [i for i in range(N)]
star_points = []
connections = []

for _ in range(N):
    star_points.append(list(map(float, input().split())))

for i in range(N):
    for j in range(i+1, N):
        dist = ((star_points[i][0] - star_points[j][0])**2 + (star_points[i][1] - star_points[j][1])**2)**(1/2)
        connections.append((i, j, round(dist, 2)))

connections.sort(key=lambda a: a[2])

ans = 0
for i in range(len(connections)):
    if find(connections[i][0]) != find(connections[i][1]):
        union(connections[i][0], connections[i][1])
        ans += connections[i][2]

print(ans)