dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dij(a, b):
    weights = []
    for _ in range(N):
        weights.append([[10000, 10000] for _ in range(N)])
    weights[a][b][0] = 1
    weights[a][b][1] = 0
    q = [(a, b, 0)]

    while q:
        x, y, break_cnt = q.pop(0)
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            chk_cnt = break_cnt
            if 0 <= nx < N and 0 <= ny < N:
                if chk_cnt > weights[nx][ny][1]:
                    continue
                temp = weights[x][y][0] + rooms[nx][ny]
                if rooms[nx][ny] == 0:
                    chk_cnt += 1
                if chk_cnt < weights[nx][ny][1]:
                    weights[nx][ny][0] = temp
                    weights[nx][ny][1] = chk_cnt
                    q.append((nx, ny, chk_cnt))
                elif chk_cnt == weights[nx][ny][1]:
                    if weights[nx][ny][0] > temp:
                        weights[nx][ny][0] = temp
                        q.append((nx, ny, chk_cnt))

    return weights[N-1][N-1][1]


N = int(input())
input_rooms = [input() for _ in range(N)]
rooms = []
for word in input_rooms:
    temp = []
    for w in word:
        temp.append(int(w))
    rooms.append(temp)

print(dij(0, 0))