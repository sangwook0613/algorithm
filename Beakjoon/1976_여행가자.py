def find(a):
    while a != city[a]:
        a = city[a]
    return a


def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        city[x] = y
    else:
        city[y] = x


N = int(input())
M = int(input())
city = [i for i in range(N+1)]
for i in range(1, N+1):
    connections = list(map(int, input().split()))
    for c in range(len(connections)):
        if connections[c]:
            union(i, c+1)
travel_plan = list(map(int, input().split()))
ans = set()
for t in travel_plan:
    ans.add(find(t))

if len(ans) == 1:
    print('YES')
else:
    print('NO')