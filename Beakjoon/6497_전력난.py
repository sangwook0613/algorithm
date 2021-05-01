def find(a):
    if a != city[a]:
        city[a] = find(city[a])
    return city[a]


def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        city[x] = y
    else:
        city[y] = x


while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    max_total = 0
    city = [i for i in range(M)]
    connections = []

    for i in range(N):
        connections.append(list(map(int, input().split())))
        max_total += connections[i][2]

    connections.sort(key=lambda a: a[2])

    total = 0
    for a, b, c in connections:
        if find(a) != find(b):
            union(a, b)
            total += c

    print(max_total - total)