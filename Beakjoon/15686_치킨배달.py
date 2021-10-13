# 15686 치킨 배달
## BFS로 어려운 계산 다해놓고 마지막에 너무 무식하게 풀려고했다,,
## 여러 경우를 항상 고려해야한다!
from itertools import combinations

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

ans = 100000
for group in list(combinations(chicken_cnt, M)):
    temp = 0
    for b in range(len(house)):
        min_length = 10000
        for a in range(len(group)):
            min_length = min(min_length, group[a][b])
        temp += min_length
    ans = min(ans, temp)

print(ans)