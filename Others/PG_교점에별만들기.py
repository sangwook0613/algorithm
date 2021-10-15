# 프로그래머스 교점에 별 만들기
## 조합을 활용한 구현 문제

from itertools import combinations


def solve(list1, list2):
    base = (list1[0] * list2[1]) - (list1[1] * list2[0])
    if base:
        x = ((list1[1] * list2[2]) - (list1[2] * list2[1])) / base
        y = ((list1[2] * list2[0]) - (list1[0] * list2[2])) / base
        return (1, x, y)
    return (0, 0, 0)


def solution(line):
    answer = []
    result = []
    for a, b in list(combinations(line, 2)):
        temp = solve(a, b)
        if temp[0] and int(temp[1]) == temp[1] and int(temp[2]) == temp[2]:
            int_point = [int(temp[1]), int(temp[2])]
            if int_point not in result:
                result.append(int_point)

    if len(result) == 1:
        return ["*"]
    height = [result[0][1], result[0][1]]
    width = [result[0][0], result[0][0]]
    for i in range(1, len(result)):
        height[0] = min(height[0], result[i][1])
        height[1] = max(height[1], result[i][1])
        width[0] = min(width[0], result[i][0])
        width[1] = max(width[1], result[i][0])

    for i in range(len(result)):
        result[i][0] = result[i][0] - width[0]
        result[i][1] = result[i][1] - height[0]

    for a in range(height[1] - height[0], -1, -1):
        stars = ''
        for b in range(width[1] - width[0] + 1):
            if [b, a] in result:
                stars += '*'
            else:
                stars += '.'
        answer.append(stars)

    return answer