# 프로그래머스 배달
## 최소비용 문제 - 다익스트라
## 무작정 풀기 전에 어떤 유형인지 먼저 생각하자!
## 다익스트라는 좀 더 공부하자

INF = int(1e9)

def solution(N, road, K):
    answer = 0
    nodes = [[] for _ in range(N+1)]
    for s, e, w in road:
        nodes[e].append((s, w))
        nodes[s].append((e, w))
            
    cost = [INF]*(N+1)
    cost[1] = 0
    q = [(1, 0)]

    while q:
        town, time = q.pop(0)
        if cost[town] < time:
            continue
        for s, w in nodes[town]:
            if cost[s] > time+w:
                cost[s] = time + w
                q.append((s, cost[s]))
            
    for c in cost:
        if c <= K:
            answer += 1
    
    return answer