# 백준 2798 블랙잭
# 입력이 100 까지이기에 완전 탐색으로 풀 수 있는 문제
def solve(n, k):
    ans = 0
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                temp = numbers[a] + numbers[b] + numbers[c]
                if temp == k:
                    return k
                if abs(M - temp) < abs(M - ans) and temp < M:
                    ans = temp
    return ans

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
print(solve(N, M))