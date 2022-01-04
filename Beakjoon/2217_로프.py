# 백준 2217 로프
## 간단한 그리디 문제
## 내림차순으로 정렬함으로 인해 그리디 접근이 가능
import sys
input = sys.stdin.readline

N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True)
ans = rope[0]

# 그리디하게 판단
for k in range(N):
    ans = max(ans, rope[k]*(k+1))

print(ans)