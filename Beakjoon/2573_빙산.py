# 2573 빙산
## 한 턴에 모든 과정이 처리된 후 결과를 바꿔야 한다!!

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cnt_icebreg(start, num):
    q = [start]
    visited[start[0]][start[1]] = 1
    cnt = 1
    while q:
        a, b = q.pop(0)
        for x, y in dxy:
            nx = a + x
            ny = b + y
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and board[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    if num == cnt:
        return False
    else:
        return True


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
iceberg = []
for i in range(R):
    for j in range(C):
        if board[i][j]:
            iceberg.append((i, j))

ans = 0
while True:
    visited = [[0] * C for _ in range(R)]
    if len(iceberg) == 0:
        print(0)
        break
    if cnt_icebreg(iceberg[0], len(iceberg)):
        print(ans)
        break
    temp = []
    make_zero = []
    for r, c in iceberg:
        for x, y in dxy:
            nr = r + x
            nc = c + y
            # 이부분이 핵심!
            # 1년이 지나기 전에 녹은 것으로 처리하면 안된다!
            # 1년에 일어나는 것은 한번에 처리하기 위해 바로 0으로 두지않고 음수로 만들어 한 해가 끝나면 처리
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 0:
                if board[r][c] == 1:
                    board[r][c] = -1
                    make_zero.append((r, c))
                elif board[r][c] > 1:
                    board[r][c] -= 1
        if board[r][c] > 0:
            temp.append((r, c))

    for ta, tb in make_zero:
        board[ta][tb] = 0

    ans += 1
    iceberg = temp[:]