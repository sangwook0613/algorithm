# 2019 KAKAO BLIND RECRUITMENT
## combinations 을 통해 부분집합을 구하는 방법
## 튜플, 셋 과 같은 파이썬 자료형을 잘 사용하면 쉬운 문제

from itertools import combinations


def chk_ans(ans, cand):
    for chk in ans:
        cnt = 0
        for c in chk:
            if c in cand:
                cnt += 1
        if cnt == len(chk):
            return False
    return True


def solution(relation):
    answer = 0
    n_row = len(relation)
    n_col = len(relation[0])
    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))

    ans = []

    for i in range(len(candidates)):
        if chk_ans(ans, candidates[i]):
            temp = []
            for j in range(n_row):
                temp_key = []
                for k in range(len(candidates[i])):
                    temp_key.append(relation[j][candidates[i][k]])
                temp.append(tuple(temp_key))

            if n_row == len(set(temp)):
                ans.append(candidates[i])

    answer = len(ans)

    return answer