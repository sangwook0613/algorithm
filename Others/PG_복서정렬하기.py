# 프로그래머스 복서 정렬하기
## 간단한 정렬 문제, lambda 활용하기


def solution(weights, head2head):
    players = [[i, weights[i]] for i in range(len(weights))]
    for i in range(len(head2head)):
        win_chk = 0
        total = len(weights)
        heavy = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'N':
                total -= 1
            if i != j and head2head[i][j] == 'W':
                win_chk += 1
                if weights[j] > weights[i]:
                    heavy += 1
        players[i] += [(win_chk / total if total else 0), heavy]

    players.sort(key=lambda a: (-a[2], -a[3], -a[1], a[0]))
    answer = [p[0] + 1 for p in players]

    return answer