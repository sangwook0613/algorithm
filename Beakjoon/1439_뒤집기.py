# 백준 1439 뒤집기
## 간단한 그리디 문제
## 연속된 0과 1들을 count 하여 그 중 작은 값을 도출
S = input()
curr = S[0]
count = [0, 0]
for s in S:
    if s != curr:
        count[int(curr)] += 1
        curr = s
count[int(curr)] += 1

print(min(count))