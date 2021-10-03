# 프로그래머스 카펫
## 또 너무 어렵게 생각하려고 했다.. 간단한 문제다

def solution(brown, yellow):
    answer = []
    brown = (brown - 4) // 2
    i = 1
    while i < brown:
        if (brown - i) * i == yellow:
            break
        i += 1

    answer = [i + 2, brown - i + 2]
    answer.sort(reverse=True)
    return answer