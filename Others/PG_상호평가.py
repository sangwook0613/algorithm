# 프로그래머스 위클리챌린지 2주차 - 상호 평가
# 간단한 수학 문제
## JS로도 꼭 풀어보자


def getGrade(arr):
    result = ''
    for a in arr:
        if a >= 90:
            result += 'A'
            continue
        elif a >= 80:
            result += 'B'
            continue
        elif a >= 70:
            result += 'C'
            continue
        elif a >= 50:
            result += 'D'
            continue
        else:
            result += 'F'
            continue
    return result


def solution(scores):
    answer = ''
    n = len(scores)
    order = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(scores[j][i])
        order.append(temp)

    avg = []
    for a in range(n):
        max_num = max(order[a])
        min_num = min(order[a])
        if max_num == order[a][a]:
            cnt = 0
            for b in order[a]:
                if b == max_num:
                    cnt += 1
            if cnt == 1:
                avg.append((sum(order[a]) - order[a][a]) / (len(order[a]) - 1))
            else:
                avg.append(sum(order[a]) / len(order[a]))
        elif min_num == order[a][a]:
            cnt = 0
            for b in order[a]:
                if b == min_num:
                    cnt += 1
            if cnt == 1:
                avg.append((sum(order[a]) - order[a][a]) / (len(order[a]) - 1))
            else:
                avg.append(sum(order[a]) / len(order[a]))
        else:
            avg.append(sum(order[a]) / len(order[a]))

    answer = getGrade(avg)
    return answer
