# 백준 6603 로또
## 간단한 재귀 문제
def solve(cnt, idx, arr):
    if cnt == 6:
        print(' '.join(arr))
        return
    for i in range(idx, N):
        arr.append(numbers[i])
        solve(cnt + 1, i + 1, arr)
        arr.pop()


while True:
    inputs = list(map(int, input().split()))
    if len(inputs) == 1:
        break
    N = inputs[0]
    numbers = [str(a) for a in inputs[1:]]
    solve(0, 0, [])
    print()