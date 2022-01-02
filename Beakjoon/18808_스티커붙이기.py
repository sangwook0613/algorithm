# 백준 18808 스티커 붙이기
## 구현 문제
## 방향을 다 바꾼 후에 붙이는 과정을 진행했기에 시간이 오래 걸림
## 방향을 필요할 때마다 바뀌는 효율적인 코드를 좀더 고민할 필요 존재
import sys
input = sys.stdin.readline

# 스티커를 붙여볼 함수
# 위에서 아래로, 왼쪽에서 오른쪽으로
def stick(board, sticker):
    for i in range(N):
        for j in range(M):
            temp = [b[:] for b in board]
            chk_break = 0
            for a in range(len(sticker)):
                for b in range(len(sticker[a])):
                    if i+a < N and j+b < M and temp[i+a][j+b] + sticker[a][b] < 2:
                        temp[i+a][j+b] += sticker[a][b]
                    else:
                        chk_break = 1
                        break
                if chk_break:
                    break
            if not chk_break:
                return True, temp
    return False, board


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
            row.append(sticker[r-1-j][i])
        r90.append(row)
    rotation.append(r90)
    # 180도 회전
    r180 = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(sticker[r-1-i][c-1-j])
        r180.append(row)
    rotation.append(r180)
    # 270도 회전
    r270 = []
    for i in range(c):
        row = []
        for j in range(r):
            row.append(sticker[j][c-1-i])
        r270.append(row)
    rotation.append(r270)

    for curr in rotation:
        chk, visited = stick(visited, curr)
        if chk:
            break

ans = 0
for v in visited:
    ans += sum(v)
print(ans)