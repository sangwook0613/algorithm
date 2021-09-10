# 백준 9466 텀 프로젝트
# DFS 응용 문제
# 흐름을 잘 이해하자! 순차적으로 이어진다!!
import sys
sys.setrecursionlimit(111111) # 충분한 재귀 깊이를 주어 오류를 예방

def dfs(s):
    temp.append(s)
    if not visited[s]:
        visited[s] = 1
        if numbers[s-1] in temp:
            global chk
            idx = temp.index(numbers[s-1])
            chk = temp[idx:]
            return
        dfs(numbers[s-1])


T = int(input())

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    visited = [0]*(N+1)
    ans = 0
    for i in range(1, N+1):
        chk = []
        temp = []
        dfs(i)
        if chk:
            ans += len(chk)

    print(N - ans)