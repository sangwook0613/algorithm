# 백준 3184 양
## BFS 를 활용하여 같은 영역의 양과 늑대를 count 하는 문제
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(start):
    q = [(start[0], start[1])]
    visited[start[0]][start[1]] = 1
    result = [0, 0]
    # start 지점에도 양이나 늑대가 있는지 체크
    if farm[start[0]][start[1]] == 'v':
        result[1] += 1
    if farm[start[0]][start[1]] == 'o':
        result[0] += 1
    while q:
        a, b = q.pop(0)
        for dx, dy in dxy:
            x = a + dx
            y = b + dy
            if 0 <= x < R and 0 <= y < C and not visited[x][y] and farm[x][y] != '#':
                visited[x][y] = 1
                q.append((x, y))
                # 양이나 늑대면 count 하기
                if farm[x][y] == 'o':
                    result[0] += 1
                if farm[x][y] == 'v':
                    result[1] += 1

    if result[1] >= result[0]:
        return 0, result[1]
    else:
        return result[0], 0


R, C = map(int, input().split())
farm = [input() for _ in range(R)]
visited = [[0]*C for _ in range(R)]
ans = [0, 0]

for i in range(R):
    for j in range(C):
        if not visited[i][j] and farm[i][j] != '#':
            sheep, wolf = bfs([i, j])
            ans[0] += sheep
            ans[1] += wolf

print(ans[0], ans[1])