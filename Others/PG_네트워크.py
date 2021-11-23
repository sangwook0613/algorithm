# 프로그래머스 네트워크
# BFS로 해결한 문제
def bfs(start, arr, visited, cnt):
    q = [start]
    while q:
        a = q.pop(0)
        for num in arr[a]:
            if not visited[num]:
                visited[num] = cnt
                q.append(num)
    return visited

def solution(n, computers):
    answer = 0
    connections = [[] for _ in range(n)]
    visited = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j]:
                connections[i].append(j)
                connections[j].append(i)
    
    t = 0
    for i in range(n):
        temp = 0
        t += 1
        for k in visited:
            if k == 0:
                break
            else:
                temp += 1
        if temp == n:
            break
        if not visited[i]:
            visited[i] = t
        visited = bfs(i, connections, visited, t)
        
    answer = set()
    for a in visited:
        answer.add(a)
    
    return len(answer)