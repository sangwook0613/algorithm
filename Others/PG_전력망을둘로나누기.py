# 프로그래머스 전력망을 둘로 나누기
## 천천히~~

def solution(n, wires):
    answer = -1
    cnt = [1]*(n+1)
    parent = [[] for _ in range(n+1)]
    for a, b in wires:
        parent[a].append(b)
    print(parent)
    for i in range(n, 0, -1):
        if len(parent[i]) != 0:
            for k in parent[i]:
                cnt[i] += cnt[k]
    print(cnt)
    return answer