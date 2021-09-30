# 프로그래머스 타켓 넘버
## BFS 로 푸는 문제
## BFS 에 접근할 수 있는 방식을 좀 더 폭 넒게 생각하자

from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    while q:
        a, b = q.popleft()
        if b == len(numbers):
            if a == target:
                answer += 1
            continue
        q.append((a + numbers[b], b + 1))
        q.append((a - numbers[b], b + 1))

    return answer