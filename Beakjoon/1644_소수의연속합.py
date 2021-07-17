# 1644 소수의 연속합
## 에라토스테네스의 체와 두 인덱스를 다룰 줄 알면 해결되는 문제
## 양 끝의 인덱스만을 관리하여 그 사이의 합을 조정하면 되는 문제


N = int(input())
numbers = []
chk = [1]*(N+1)
idx = 2
ans = 0

while idx <= N:
    if chk[idx]:
        numbers.append(idx)
        for i in range(idx*2, N+1, idx):
            chk[i] = 0
    idx += 1

total = 0
end = 0
for start in range(len(numbers)):
    while total < N and end < len(numbers):
        total += numbers[end]
        end += 1

    if total == N:
        ans += 1
    total -= numbers[start]

print(ans)