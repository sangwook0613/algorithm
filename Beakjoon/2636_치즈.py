# 2636 치즈
## 최대 100*100 이기에 BFS로 간단하게 풀 수 있는 문제

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(start, arr):
    q = [start]
    visited[start[0]][start[1]] = 1
    melt_point = []
    while q:
        r, c = q.pop(0)
        for x, y in dxy:
            nx = r + x
            ny = c + y
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    melt_point.append((nx, ny))

    return melt_point


def cnt_cheese(arr):
    total = 0
    for a in arr:
        total += sum(a)
    return total


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

cnt = 1
ans = cnt_cheese(board)
a = b = 0
while True:
    visited = [[0]*C for _ in range(R)]
    melt = bfs((a, b), board)

    for i, j in melt:
        board[i][j] = 0

    temp = cnt_cheese(board)
    if temp == 0:
        break
    else:
        ans = temp
        cnt += 1

print(cnt)
print(ans)