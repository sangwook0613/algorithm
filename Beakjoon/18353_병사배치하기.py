# 백준 18353 병사 배치하기
## DP 를 활용하는 최장 증가 부분 수열 알고리즘을 활용하는 문제
### 원리는 i를 1 부터 N 까지 차근차근 증가하면서
### 그 때 i 보다 작은 인덱스를 갖는 값 중에서 작은 값인지 판단
### 만약 있다면 그 dp 배열의 값에 + 1을 하면서 갱신해나가는 것
N = int(input())
soldiers = list(map(int, input().split()))
count = [1]*N
ans = 2000
for i in range(1, N):
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            count[i] = max(count[i], count[j]+1)
        ans = min(ans, N - count[i])

print(ans if ans != 2000 else 0)