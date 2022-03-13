# 백준 18405 경쟁적 전염
## BFS 를 활용한 문제
## 입력에서 n 번의 바이러스가 딱 하나만 있지 않을 경우를 고려해야 한다!
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
s, x, y = map(int, input().split())
virus = [[] for _ in range(K+1)]

# n 번 바이러스가 여러개 있을 것을 고려하여 모두 append 한다.
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            virus[board[i][j]].append([i, j, 0])

# 이후 큐에 넣을 때, extend 를 통해 한번에 처리
q = []
for i in range(1, K+1):
    if len(virus[i]):
        q.extend(virus[i])

while q:
    a, b, c = q.pop(0)
    if c == s:
        break
    for dx, dy in dxy:
        da = a + dx
        db = b + dy
        if 0 <= da < N and 0 <= db < N and not board[da][db]:
            board[da][db] = board[a][b]
            q.append([da, db, c+1])

print(board[x-1][y-1])