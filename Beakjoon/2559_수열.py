# 백준 2559 수열
## 누적합 문제!
## '누적' 합이다! 누적한걸 잘 활용해보자!
N, K = map(int, input().split())
temp = list(map(int, input().split()))
total = [0]
for t in range(N):
    total.append(temp[t] + total[t])

ans = -10000000
for i in range(N-K+1):
    ans = max(ans, total[i+K]-total[i])

print(ans)

## 더하고 빼고를 활용해서 누적합
N, K = map(int, input().split())
Tmp = list(map(int, input().split()))

TmpSum = sum(Tmp[:K])
Tmp_result = [TmpSum]

for i in range(len(Tmp)-K):
    TmpSum = TmpSum - Tmp[i] + Tmp[i+K]
    Tmp_result.append(TmpSum)

print(max(Tmp_result))