# 프로그래머스 짝지어 제거하기
## 간단한 스택 문제

def solution(word):
    words = []
    for w in word:
        if len(words) == 0:
            words.append(w)
        else:
            if words[-1] == w:
                words.pop()
            else:
                words.append(w)

    if len(words):
        return 0
    else:
        return 1