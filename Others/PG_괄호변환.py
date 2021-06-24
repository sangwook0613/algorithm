# 2020 KAKAO BLIND RECRUITMENT - 괄호 변환

## 카카오가 좋아하는 문자열 다루기
## 재귀에 대한 이해도가 있으면 쉽게 풀 수 있는 문제


def chk_balance(s):
    start = 0
    for i in range(len(s)):
        if start < 0:
            return False
        if s[i] == '(':
            start += 1
        else:
            start -= 1
    if start == 0:
        return True
    return False


def divide(s):
    start = idx = 0
    for i in range(len(s)):
        if i != 0 and start == 0:
            idx = i
            break
        if s[i] == '(':
            start += 1
        else:
            start -= 1
    if idx == 0:
        idx = len(s)
    return s[:idx], s[idx:]


def solution(p):
    if len(p) == 0:
        return ''

    u, v = divide(p)

    if chk_balance(u):
        return u + solution(v)
    else:
        ans = '(' + solution(v) + ')'

        for a in range(1, len(u) - 1):
            if u[a] == '(':
                ans += ')'
            else:
                ans += '('
    return ans