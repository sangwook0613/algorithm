# 백준 18222 투에-모스 문자열
## 2의 제곱수들을 빼나가면서 1까지 도달하는데까지 빼는 횟수를 count 하여 계산
k = int(input())
cnt = 0
pow2 = [1] # k 보다 작은 2의 제곱수들을 모아둘 배열
temp = 1
while temp < k:
    temp *= 2
    pow2.append(temp)

for i in range(len(pow2)-1, -1, -1):
    # pow2 를 역순으로 보면서 k 보다 작은 경우에만 빼고 cnt + 1 & k 업데이트
    if k > pow2[i]:
        k -= pow2[i]
        cnt += 1

# 홀수면 1을 짝수면 0을 출력
print(1 if cnt % 2 else 0)