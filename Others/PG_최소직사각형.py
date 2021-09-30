# 프로그래머스 최소직사각형
## 진짜 이런거를 바로바로 못푸는건 문제가 있다...
## 좀 더 분발하자..

def solution(sizes):
    answer = 0
    max_num = 0
    min_nums = []
    for i in range(len(sizes)):
        min_nums.append(min(sizes[i]))
        max_num = max(max_num, max(sizes[i]))

    answer = max_num * max(min_nums)
    return answer