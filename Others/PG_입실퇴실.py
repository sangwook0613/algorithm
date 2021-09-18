# 프로그래머스 입실 퇴실
# 문제 그대로 풀면되는 간단한 문제, 괜히 어렵게 생각했다.

def solution(enter, leave):
    answer = [0] * len(enter)
    current = [enter.pop(0)]
    while leave:
        if leave[0] in current:
            current.remove(leave[0])
            for c in current:
                answer[c - 1] += 1
            answer[leave[0] - 1] += len(current)
            leave.pop(0)
            continue
        current.append(enter.pop(0))

    return answer