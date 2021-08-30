# 프로그래머스
## 생각해보면 정말 단순한 문제
## 너무 어렵게만 생각하지 말자...

def solution(priorities, location):
    paper = [(p, i) for i, p in enumerate(priorities)]
    ans = []

    while paper:
        num, idx = paper.pop(0)
        temp = [p for p, i in paper]
        max_num = 0
        if temp:
            max_num = max(temp)

        if num >= max_num:
            ans.append(idx)
        else:
            paper.append((num, idx))

    for a in range(len(ans)):
        if ans[a] == location:
            return a + 1