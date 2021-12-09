# 백준 9046 복호화
## 간단한 문자열 처리 문제
## 딕셔너리를 활용
T = int(input())

for _ in range(T):
    count = {}
    words = input()
    for w in words:
        if w == ' ':
            continue
        if count.get(w):
            count[w] += 1
        else:
            count[w] = 1

    max_cnt = 0
    ans = []
    for key, value in count.items():
        if value > max_cnt:
            max_cnt = value
            ans = [key]
        elif value == max_cnt:
            ans.append(key)

    if len(ans) > 1:
        print('?')
    else:
        print(ans[0])