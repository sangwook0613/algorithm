BIG = int(1e9)
def dij(start, end, k):
    weight = [BIG]*(N+1)
    weight[start] = k
    q = [start]

    while q:
        num = q.pop(0)
        for x, w in nodes[num]:
            temp = weight[num] + w
            if weight[x] > temp:
                weight[x] = temp
                q.append(x)

    return weight[end]


N, E = map(int, input().split())
nodes = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))

p1, p2 = map(int, input().split())

order1 = [1, p1, p2, N]
order2 = [1, p2, p1, N]

ans1 = ans2 = 0

for i in range(3):
    ans1 = dij(order1[i], order1[i+1], ans1)
    ans2 = dij(order2[i], order2[i+1], ans2)

ans = min(ans1, ans2)
if ans >= BIG:
    print(-1)
else:
    print(ans)