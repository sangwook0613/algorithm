# 백준 4963 섬의 개수
## BFS 활용해서 풀이
## List index만 조심! 대각선까지 8개의 방향을 모두 고려해야한다
dxy = [(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)] # 상하좌우 대각선


def bfs(start, arr, chk):
    q = [start]
    visited[start[0]][start[1]] = chk
    while q:
        r, c = q.pop(0)
        for dx, dy in dxy:
            x = r + dx
            y = c + dy
            if 0 <= x < b and 0 <= y < a and arr[x][y] == 1 and not visited[x][y]:
                q.append((x, y))
                visited[x][y] = chk


while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    board = [list(map(int, input().split())) for _ in range(b)]
    visited = [[0]*a for _ in range(b)]
    lands = []
    for i in range(b):
        for j in range(a):
            if board[i][j]:
                lands.append((i, j))

    ans = 0
    for p in lands:
        if not visited[p[0]][p[1]]:
            ans += 1
            bfs(p, board, ans)

    print(ans)