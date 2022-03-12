# 백준 18405 경쟁적 전염
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
s, x, y = map(int, input().split())

for i in range(N):
    for j in range(N):
        