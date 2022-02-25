# 백준 2302 극장 좌석
## 경우의 수를 구해서 풀면되는 간단한 문제
## VIP 자석을 기준으로 좌석을 나누면 그룹을 형성할 수 있고 각 그룹들에서 배치될 수 있는 경우의 수를 모두 구하고 곱하면되는 문제
### 경우의 수에 규칙이 있다! 피보나치 수열을 따라 증가한다.
N = int(input())
M = int(input())
seats = [0]*N # VIP 좌석을 체크하기 위한 배열
for _ in range(M):
    seats[int(input()) - 1] = 1

groups = [] # VIP 좌석을 기준으로 나눈 그룹을 담을 배열
temp = []
max_length = 0 # 가장 큰 그룹의 길이
# 그룹으로 나누기
for i in range(N):
    if seats[i]:
        if len(temp):
            groups.append(temp)
            max_length = max(len(temp), max_length)
        temp = []
    else:
        temp.append(i)

if len(temp):
    groups.append(temp)
    max_length = max(len(temp), max_length)

count = [1, 1] # 피보나치 수열의 값을 담을 배열
idx = 1
# 최대 그룹의 길이만큼 피보나치 수열을 구한다.
while idx < max_length:
    count.append(count[idx] + count[idx-1])
    idx += 1

# 각각의 경우의 수를 곱해서 출력
ans = 1
for g in groups:
    ans *= count[len(g)]

print(ans)