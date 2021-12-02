# 백준 피보나치수7
# DP로 반복문을 돌려서 풀었다
# 나머지를 구하는 것이기에 애초에 나머지만 보관하면 된다! 그러지 않으면 메모리 초과!!
N = int(input())
arr = [0]*(N+1)
if N >= 1:
    arr[1] = 1
for i in range(2, N+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 1000000007

print(arr[N])