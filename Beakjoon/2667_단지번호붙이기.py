def DFS(a, b, k):
    if a < 0 or a > N-1 or b < 0 or b > N-1:
        return False
    if board[a][b] == 1 and visited[a][b] == 0:
        visited[a][b] = k
        DFS(a-1, b, k)
        DFS(a, b-1, k)
        DFS(a+1, b, k)
        DFS(a, b+1, k)
        return True
    return False


N = int(input())
board = []
for i in range(N):
    text = input()
    temp = []
    for j in range(N):
        if text[j] == '0':
            temp += [0]
        else:
            temp += [1]
    board += [temp]

visited = [[0]*N for _ in range(N)]
cnt = 1
ans = 0
for i in range(N):
    for j in range(N):
        if DFS(i, j, cnt):
            ans += 1
            cnt += 1

ans_list = []
for a in range(1, ans+1):
    temp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == a:
                temp += 1
    ans_list += [temp]

ans_list.sort()
print(ans)
for i in ans_list:
    print(i)