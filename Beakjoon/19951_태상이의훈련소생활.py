# 백준 19951 태상이의 훈련소 생활
## 가스조절기 잃어버리지 말자...
## 최대가 10만x10만 이기에 누적합을 통해 풀이
## a부터 b의 구간이 아닌 a와 b의 길이를 갖는 막대가 2개를 입력으로 받는다 해석하면 쉽게 접근 가능
N, M = map(int, input().split())
ground = list(map(int, input().split()))
count = [0]*(N+1)
for _ in range(M):
    a, b, h = map(int, input().split())
    # 2개의 막대로 구분해서 input을 정리
    count[b] += h
    count[a-1] += -h

# 누적합 계산
for i in range(N, 0, -1):
    count[i-1] += count[i]

for i in range(1, N+1):
    print(ground[i-1] + count[i], end=' ')