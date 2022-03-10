# 백준 1158 요세푸스 문제
from collections import deque
N, K = map(int, input().split())
numbers = deque([i for i in range(1, N+1)])
result = []
cnt = 0
while numbers:
    cnt += 1
    if cnt == K:
        result.append(numbers.popleft())
        cnt = 0
    else:
        numbers.append(numbers.popleft())

print('<', end='')
for r in range(N):
    print(result[r], end='')
    if r != N-1:
        print(', ', end='')
print('>')