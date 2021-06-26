# 문자열 다루는 문제
# 파이썬이여서 더 쉽게 풀 수 있는 문제

def solution(str1, str2):
    answer = 65536

    first = []
    second = []
    for i in range(len(str1) - 1):
        if ('a' <= str1[i] <= 'z' or 'A' <= str1[i] <= 'Z') and (
                'a' <= str1[i + 1] <= 'z' or 'A' <= str1[i + 1] <= 'Z'):
            first.append(str1[i:i + 2].lower())

    for i in range(len(str2) - 1):
        if ('a' <= str2[i] <= 'z' or 'A' <= str2[i] <= 'Z') and (
                'a' <= str2[i + 1] <= 'z' or 'A' <= str2[i + 1] <= 'Z'):
            second.append(str2[i:i + 2].lower())

    union = []
    chk = [0] * len(second)
    for a in first:
        for b in range(len(second)):
            if a == second[b] and not chk[b]:
                union.append(second[b])
                chk[b] = 1
                break

    if len(first) != 0 or len(second) != 0:
        answer = int(len(union) / (len(first) + len(second) - len(union)) * 65536)
    return answer