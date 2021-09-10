# 백준 10451 순열 사이클
# DFS를 통해 꼬리를 물어가는 문제

def dfs(s, n):
    if not visited[s]:
        visited[s] = n
        dfs(numbers[s-1], n)

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    visited = [0]*(N+1)
    cnt = 1
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = cnt
            dfs(numbers[i-1], cnt)
            cnt += 1

    print(cnt - 1)