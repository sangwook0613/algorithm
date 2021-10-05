# 15686 치킨 배달

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(r, c):
    q = [(r, c, 0)]
    visited[r][c] = 1
    while q:
        a, b, cnt = q.pop(0)
        for dx, dy in dxy:
            x = a + dx
            y = b + dy
            if 0 <= x < N and 0 <= y < N and not visited[x][y]:
                visited[x][y] = 1
                q.append((x, y, cnt+1))
                if city[x][y] == 2:
                    for i in range(len(chicken)):
                        if chicken[i] == (x, y):
                            chicken_cnt[i].append(cnt+1)


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        if city[i][j] == 2:
            chicken.append((i, j))

chicken_cnt = [[] for _ in range(len(chicken))]
for r, c in house:
    visited = [[0]*N for _ in range(N)]
    bfs(r, c)

max_cnt = []
for i in range(len(chicken_cnt)):
    max_cnt.append((i, sum(chicken_cnt[i])))
max_cnt.sort(key= lambda x: x[1])

result = []
for i in range(len(max_cnt[:M])):
    result.append(chicken_cnt[max_cnt[i][0]])

ans = 0
for c in range(len(result[0])):
    temp = 100000
    for r in range(len(result)):
        temp = min(temp, result[r][c])
    ans += temp
print(ans)