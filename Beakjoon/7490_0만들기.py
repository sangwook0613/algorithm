# 백준 7490 0 만들기
## 재귀를 활용한 완전 탐색 문제
## 파이썬이기에 문자열을 간단하게 처리할 수 있었던 문제 (람다 활용)
caculator = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
}
symbols = [' ', '+', '-']


def getNum(num, order):
    new_num = [1]
    for i in range(num-1):
        if order[i] == ' ':
            new_num.append(new_num.pop()*10 + i+2)
        else:
            new_num.append(i + 2)
    idx = 0
    result = new_num[0]
    for i in range(num-1):
        if order[i] == ' ':
            continue
        result = caculator[order[i]](result, new_num[idx+1])
        idx += 1
    return result


def solve(cnt, arr, n):
    if cnt == n:
        if getNum(n, arr) == 0:
            ans = '1'
            for k in range(n-1):
                ans += arr[k] + str(k+2)
            print(ans)
        return
    for i in range(3):
        arr.append(symbols[i])
        solve(cnt+1, arr, n)
        arr.pop()


T = int(input())

for _ in range(T):
    N = int(input())
    solve(1, [], N)
    print()