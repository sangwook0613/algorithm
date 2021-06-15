N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

memo = [0]*N
memo[0] = numbers[0]
if N >= 2:
    memo[1] = max(numbers[0] + numbers[1], numbers[0]*numbers[1])

for i in range(2, N):
    memo[i] = max(memo[i-1] + numbers[i], memo[i-2] + numbers[i-1]*numbers[i])

print(memo[N-1])