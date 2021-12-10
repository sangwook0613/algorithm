# 백준 13707 합분해 2
## 배열을 통해 이전 값들의 합을 저장해놓고 풀이
## pypy3 는 통과하지만 python3는 시간초과
N, K = map(int, input().split())

numbers = [[1] + [0]*(K-1) for _ in range(N)]
for i in range(1, K):
    numbers[0][i] = i+1

for a in range(1, N):
    for b in range(1, K):
        numbers[a][b] = (numbers[a][b-1] + numbers[a-1][b]) % 1000000000

print(numbers[N-1][K-1])


# python3 pypy3 모두 통과하는 풀이
## 조합으로 풀어낼 수 있는 규칙을 찾음
## (N+K-1) C (K-1)
N, K = map(int, input().split())

top = 1
bottom = 1
for i in range(N+K-1, N, -1):
    top *= i
    bottom *= (N+K-i)
print((top // bottom) % 1000000000)