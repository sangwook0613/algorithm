# 백준 9466 텀 프로젝트
## DFS 응용 문제
## 한번씩 쭉 살펴보면서 사이클이 있다면, 사이클을 파악하여 count하는 방법
## 배열을 무작정 생성하면 시간을 많이 먹는것 같다. 이 부분은 항상 유념하자!
import sys
sys.setrecursionlimit(111111) # 충분한 재귀 깊이를 주어 오류를 예방

def dfs(s):
    visited[s] = 1
    chk.append(s)
    # 만약 해당 학생의 선택의 결과가 이미 visited 되었다면
    if visited[numbers[s]]:
        global result
        # 그 결과가 chk 에 있는지 판단하고
        if numbers[s] in chk:
            # 있다면, 그 때 그 위치의 인덱스를 뽑고
            idx = chk.index(numbers[s])
            # 사이클의 배열을 result에 추가
            result += chk[idx:]
        return
    else:
        dfs(numbers[s])


T = int(input())

for _ in range(T):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [0]*(N+1)
    ans = 0
    result = []
    for i in range(1, N+1):
        if not visited[i]:
            chk = []
            dfs(i)

    print(N - len(result))