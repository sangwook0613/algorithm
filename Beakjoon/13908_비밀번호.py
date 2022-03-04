# 백준 13908 비밀번호
## 브루트 포스를 활용한 풀이 (pypy3) 만 통과
## python3 를 통화하기 위해서는 포함배제의 원리에 따른 계산이 필요
def solve(cnt, arr):
    if cnt == N:
        temp = 0
        for a in numbers:
            temp += 1 if arr[a] else 0
        if temp == M:
            global ans
            ans += 1
        return
    for i in range(10):
        if chk[i]:
            arr[i] += 1
        solve(cnt + 1, arr)
        arr[i] -= 1


N, M = map(int, input().split())
numbers = list(map(int, input().split())) if M else []
chk = [0]*10
for num in numbers:
    chk[num] = 1

if M == 0:
    print(10**N)
else:
    ans = 0
    solve(0, [0]*10)
    print(ans)