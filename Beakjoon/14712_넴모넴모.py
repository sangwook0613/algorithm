# 백준 14712 넴모넴모 Easy
## DFS 를 활용하여 모든 경우를 다 찾아보는 방식으로 풀이
## 이 때, 네모가 될 수 있는 경우는 제외하는 가지치기 진행
### N*M 배열을 만들때 인덱스를 하나씩 늘려서 (N+1)*(M+1) 배열로 처리했기에 좀 더 용이하게 네모 판별이 가능했음
def dfs(a, b):
    # 가장 마지막 칸까지 도달한 경우
    ## ans 를 하나 늘리고 return
    if a == N and b > M:
        global ans
        ans += 1
        return

    # 열이 끝난 경우, 갱신
    if b > M:
        a += 1
        b = 1

    # (a, b) 를 빈칸으로 두고 넘어감
    dfs(a, b+1)

    # (a, b) 를 채우고 넘어감
    ## 채웠을 때 2*2 네모가 되는지 판단
    if not (board[a-1][b-1] and board[a][b-1] and board[a-1][b]):
        board[a][b] = 1
        dfs(a, b+1)
        # 나왔으면 다시 원상복구
        board[a][b] = 0


N, M = map(int, input().split())
board = [[0]*(M+1) for _ in range(N+1)]
ans = 0

dfs(1, 1)
print(ans)


# 시간초과난 풀이
## 2*2 네모가 만들어진 경우를 구하고 거기서 하나씩 넣어보면서 네모가 게임을 더 진행하는 모든 경우를 구한 후
## 모든 경우의 수에서 빼는 방식으로 진행하려고 함
## BUT 시간 초과 - 아마 게임을 진행할 수 있는 모든 경우의 수를 구하는데서 시간초과가 나는 듯
def set_square(r, c):
    result = ['0']*(N*M)
    for a in range(2):
        for b in range(2):
            if r + a < N and j + b < M:
                result[(r+a)*M+(j+b)] = '1'
            else:
                return False, ['0']*(N*M)
    return True, result


N, M = map(int, input().split())
visited = [0]*(2**(N*M+1))
q = []
for i in range(N):
    for j in range(M):
        chk, result = set_square(i, j)
        if chk:
            q.append(result)
            visited[int(''.join(result), 2)] = 1

while q:
    arr = q.pop(0)
    for i in range(N*M):
        if arr[i] != '1':
            new_arr = arr[:]
            new_arr[i] = '1'
            temp = int(''.join(new_arr), 2)
            if not visited[temp]:
                q.append(new_arr)
                visited[temp] = 1

print(2**(N*M) - sum(visited))