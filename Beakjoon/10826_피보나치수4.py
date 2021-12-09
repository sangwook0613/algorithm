# 백준 10826 피보나치 수4
N = int(input())
arr = [0]*(N+1)
if N >= 1:
    arr[1] = 1
for i in range(2, N+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[N])