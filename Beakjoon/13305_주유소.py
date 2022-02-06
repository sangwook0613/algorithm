# 백준 13305 주유소
## 그리디 알고리즘을 풀면되는 문제
## 현재 도시의 기름값이 다음 도시의 기름값보다 싼지 확인해서 싸다면 이동거리만큼 더 사고 그렇지 않으면 다음 도시가서 기름을 사는 식
N = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
ans = 0
idx = before = 0

while idx < N - 1:
    if city[before] > city[idx+1]:
        ans += city[before]*sum(road[before:idx+1])
        before = idx + 1
    idx += 1

if before != idx:
    ans += city[before]*sum(road[before:idx+1])

print(ans)