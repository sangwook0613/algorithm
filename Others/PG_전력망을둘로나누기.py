# 프로그래머스 전력망을 둘로 나누기
## 유니온파인드로 풀었는데도 아니다.. 왜??
## 유니온파인드에서 추가적으로 부모 노드를 맞추는 과정이 필요한것 같다
## 우선 더 단순한 BFS로 풀었다. 원리는 같다!

def bfs(visited, connections, start):
    cnt = 0
    q = [start]
    visited[start] = 1
    while q:
        k = q.pop(0)
        cnt += 1
        for n in connections[k]:
            if not visited[n]:
                visited[n] = 1
                q.append(n)
    return cnt


def solution(n, wires):
    answer = 1000
    for i in range(len(wires)):
        visited = [0] * (n + 1)
        temp = wires[:i] + wires[i + 1:]
        connections = [[] for _ in range(n + 1)]
        for a, b in temp:
            connections[a].append(b)
            connections[b].append(a)
        result = bfs(visited, connections, wires[i][0])
        answer = min(answer, abs(result - (n - result)))

    return answer