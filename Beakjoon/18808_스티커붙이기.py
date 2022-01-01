# 백준 18808 스티커 붙이기
N, M, K = map(int, input().split())
stickers = []
for _ in range(K):
    r, c = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(r)]
    