# 백준 18808 스티커 붙이기
# 스티커를 붙여볼 함수
# 위에서 아래로, 왼쪽에서 오른쪽으로
def stick(board, sticker):
    temp = [b[:] for b in board]
    for i in range(N):
        for j in range(M):
            # 붙일 수 있다면
            if board[i][j] + sticker[i][j] < 2:
                board[i][j] = 1
            else:
                return False, temp
    return True, board

N, M, K = map(int, input().split())
visited = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    rotation = [sticker]
    # 90도 회전
    r90 = []
    for i in range(c):
        row = []
        for j in range(r):
            row.append(sticker[r-1-j][c])
        r90.append(row)
    rotation.append(r90)
    # 180도 회전
    r180 = []

    # 270도 회전
    r270 = []
    for i in range():
        row = []
        for j in range():
            pass

