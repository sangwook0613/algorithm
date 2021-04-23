BIG = int(1e9)

def dij(start, arr):
    weight = [0] + [BIG]*N
    weight[start] = 0
    q = [start]

    while q:
        a = q.pop(0)
        for i, w in arr[a]:
            temp = weight[a] + w
            if temp < weight[i]:
                weight[i] = temp
                q.append(i)

    return weight


N, M, X = map(int, input().split())
board = [[]*N for _ in range(N+1)]
transpose = [[]*N for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    chk = 0
    for w in range(len(board[start])):
        if board[start][w][0] == end:
            board[start][w][1] = min(board[start][w][1], weight)
            chk = 1
            break
    if chk:
        continue
    board[start].append([end, weight])
    transpose[end].append([start, weight])

board_dij = dij(X, board)
transpose_dij = dij(X, transpose)
ans = 0
for i in range(1, N+1):
    ans = max(ans, board_dij[i] + transpose_dij[i])
print(ans)