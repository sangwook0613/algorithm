# 우 상 하 좌
dxy = [(0, 1), (-1, 0), (1, 0), (0, -1)]

N = int(input())
board = [[-1]*(N+2)]
board += [[-1] + [0]*N + [-1] for _ in range(N)]
board.append([-1]*(N+2))

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1

L = int(input())
snake_dir = [list(input().split()) for _ in range(L)]

# 우 - 상하 / 상 - 좌우 / 하 - 우좌 / 좌 - 하상
change_dir = [(1, 2), (3, 0), (0, 3), (2, 1)]
now_dir = 0
point = [1, 1]
visited = [point]
idx = 0
sec = 0
while True:
    if idx < L:
        if sec == int(snake_dir[idx][0]):
            now_dir = change_dir[now_dir][0 if snake_dir[idx][1] == 'L' else 1]
            idx += 1

    new_point = [point[0]+dxy[now_dir][0], point[1]+dxy[now_dir][1]]
    if board[new_point[0]][new_point[1]] < 0 or new_point in visited:
        sec += 1
        break
    if board[new_point[0]][new_point[1]]:
        board[new_point[0]][new_point[1]] = 0
    else:
        visited.pop(0)
    visited.append(new_point)
    point = new_point
    sec += 1

print(sec)