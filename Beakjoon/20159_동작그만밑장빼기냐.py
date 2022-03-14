# 백준 20159 동작 그만. 밑장 빼기냐?
N = int(input())
numbers = list(map(int, input().split()))
even_numbers = [numbers[n] for n in range(0, N, 2)]

even_idx = 0 # 내 카드 중에서 가장 작은 수의 인덱스
odd_idx = 1 # 친구 카드 중에서 가장 큰 수의 인덱스
for i in range(2, N):
    if i % 2 == 0 and numbers[even_idx] > numbers[i]:
        even_idx = i
    if i % 2 and numbers[odd_idx] < numbers[i]:
        odd_idx = i

temp = numbers[-1] - numbers[even_idx]
temp2 = numbers[odd_idx] - numbers[-1]

ans = 0
if temp > temp2:
    for n in range(0, even_idx, 2):
        ans += numbers[n]
    for n in range(even_idx+1, N, 2):
        ans += numbers[n]
else:
    for n in range(0, odd_idx, 2):
        ans += numbers[n]
    for n in range(odd_idx, N, 2):
        ans += numbers[n]
    ans -= numbers[-1]

print(ans if ans > sum(even_numbers) else sum(even_numbers))