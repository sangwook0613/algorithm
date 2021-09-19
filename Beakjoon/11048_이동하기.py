# 11048 이동하기
## BFS 인줄 알았으나 3의 1000제곱이기에 시간초과가 난다
## DP로 다시 풀어보자

from collections import deque
dxy = [(0, 1), (1, 0), (1, 1)]


def bfs(i, j, k):
    q = deque([(i, j, k)])

    while q:
        x, y, cur = q.popleft(0)
        for dx, dy in dxy:
            a = x + dx
            b = y + dy
            if 0 <= a < N and 0 <= b < M:
                count[a][b] = max(count[a][b], board[a][b]+cur)
                q.append((a, b, count[a][b]))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
count = [[0]*M for _ in range(N)]
bfs(0, 0, board[0][0])
print(count[N-1][M-1])