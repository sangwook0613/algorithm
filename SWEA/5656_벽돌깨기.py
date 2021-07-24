# 5656 벽돌 깨기
## 행, 열 인덱스을 잘 다룰 줄 알면, bfs로 풀리는 문제


import copy

# 공 순서 정하는 함수
def get_order(idx, arr):
    if idx == N:
        temp = [n for n in arr]
        orders.append(temp)
        return
    for i in range(W):
        arr.append(i)
        get_order(idx+1, arr)
        arr.pop()


# 아래로 내려주는 함수
def set_bricks(arr):
    for w in range(W):
        temp = []
        for h in range(H):
            if arr[h][w]:
                temp.append(arr[h][w])
                arr[h][w] = 0
        for k in range(H-len(temp), H):
            arr[k][w] = temp[k-(H-len(temp))]
    return arr

# 벽돌 꺠는 함수 - bfs
def break_bricks(start, arr):
    q = [start]
    arr[start[0]][start[1]] = 0
    while q:
        x, y, bomb = q.pop(0)
        if bomb <= 0:
            continue
        for a in range(-bomb, bomb+1):
            nx = x + a
            ny = y
            if x != nx and 0 <= nx < H and 0 <= ny < W and arr[nx][ny] > 0:
                q.append((nx, ny, arr[nx][ny]-1))
                arr[nx][ny] = 0
            nx = x
            ny = y + a
            if y != ny and 0 <= nx < H and 0 <= ny < W and arr[nx][ny] > 0:
                q.append((nx, ny, arr[nx][ny]-1))
                arr[nx][ny] = 0

    arr = set_bricks(arr)
    return arr


T = int(input())

for t in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    orders = []
    get_order(0, [])

    ans = 1000
    for order in orders:
        temp_bricks = copy.deepcopy(bricks)
        total = 0
        if ans == 0:
            break
        for o in order:
            for h in range(H):
                if temp_bricks[h][o]:
                    temp_bricks = break_bricks((h, o, temp_bricks[h][o]-1), temp_bricks)
                    break
        for tb in temp_bricks:
            for n in tb:
                if n:
                    total += 1
        ans = min(ans, total)

    print('#%d %d' % (t, ans))
