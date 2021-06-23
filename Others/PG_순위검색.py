from itertools import combinations

# 딕셔너리 활용
# 조합 라이브러리 사용
# 마지막으로, 이진 탐색 사용을 요구하는 문제


def solution(infos, query):
    info_dict = {}
    for info in infos:
        info = info.split()
        score = int(info[-1])
        info = info[:-1]

        for n in range(5):
            for combi in combinations(info, n):
                temp = ''.join(combi)

                if temp in info_dict.keys():
                    info_dict[temp].append(score)
                else:
                    info_dict[temp] = [score]

    for v in info_dict.values():
        v.sort()

    answer = []
    for q in query:
        q = q.replace('and', '').replace('-', '').split()
        q_score = int(q[-1])
        key = ''.join(q[:-1])

        if key in info_dict.keys():
            if len(q) == 1:
                scores = info_dict['']
            else:
                scores = info_dict[key]

            left = 0
            right = len(scores)
            while left <= right and left < len(scores):
                mid = (left + right) // 2
                if scores[mid] >= q_score:
                    right = mid - 1
                else:
                    left = mid + 1
            answer.append(len(scores) - left)
        else:
            answer.append(0)
    return answer