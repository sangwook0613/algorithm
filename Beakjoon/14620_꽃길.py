# 백준 14620 꽃길
## 간단한 DFS 와 백트래킹을 사용하는 문제
dxy = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(a, cnt, total, arr):
    global ans
    if cnt == 3:
        ans = min(ans, total)
        return

    # 현재 ans보다 크면 더 볼 필요가 없다.
    if total > ans:
        return

    for b in range(a, len(available_points)):
        i, j = available_points[b]
        flag = False
        for dx, dy in dxy:
            if visited[i+dx][j+dy]:
                flag = True
                break

        # 다른 구역을 칩입하지 않으면 진행
        if not flag:
            for dx, dy in dxy:
                visited[i+dx][j+dy] = 1
                total += ground[i+dx][j+dy]
            dfs(b+1, cnt+1, total, arr+[b])
            for dx, dy in dxy:
                visited[i+dx][j+dy] = 0
                total -= ground[i+dx][j+dy]


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
available_points = []
ans = 200*5*3

# 가능한 포인트만 확인하기
for i in range(1, N-1):
    for j in range(1, N-1):
        available_points.append((i, j))

dfs(0, 0, 0, [])
print(ans)