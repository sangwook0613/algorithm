def find(a):
    if a != house[a]:
        house[a] = find(house[a])
    return house[a]

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        house[x] = y
    else:
        house[y] = x


N, M = map(int, input().split())
house = [i for i in range(N+1)]
roads = []

for _ in range(M):
    roads.append(list(map(int, input().split())))

roads.sort(key=lambda a: a[2])

ans = 0
last_road = 0
for k in range(M):
    if find(roads[k][0]) != find(roads[k][1]):
        union(roads[k][0], roads[k][1])
        ans += roads[k][2]
        last_road = roads[k][2]

# MST를 완성한 다음, 가장 마지막 길을 삭제하여
# 유지비가 가장 적은 2개의 마을을 구성
ans -= last_road
print(ans)