# 백준 20159 동작 그만. 밑장 빼기냐?
n = int(input())
x = list(map(int,input().split()))

cards_sum = [[0] * (n//2 + 1)] + [[0] * (n//2 + 1)]


for i in range(n):
    # 짝수 인덱스일 경우
    if not (i+1) % 2:
        cards_sum[0][i//2+1] = cards_sum[0][i//2] + x[i]
    # 홀수 인덱스일 경우
    else:
        cards_sum[1][i//2+1] = cards_sum[1][i//2] + x[i]

max_value = 0
result = [0] * (n+1)
for i in range(1,n+1):
    idx = i//2 + 1
    # 짝수 인덱스일 경우
    if not i % 2:
        result[i] = cards_sum[1][idx-1] + cards_sum[0][n//2-1] - cards_sum[0][idx-2]
    else:
        result[i] = cards_sum[1][idx-1] + (cards_sum[0][n//2-1]-cards_sum[0][idx-1]) + x[n-1]
    max_value = max(result[i],max_value)

print(max_value)