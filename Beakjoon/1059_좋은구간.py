# 백준 1059 좋은 구간
L = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
N = int(input())
min_num = 0
max_num = 0
chk = False
for i in numbers:
    if i < N:
        min_num = i
    elif i == N:
        chk = True
        break
    else:
        max_num = i
        break

# n 이 집합에 있다면 무조건 0
if chk:
    print(0)
else:
    # n 보다 작은 수 x n 보다 큰 수
    # 이 때, A 혹은 B 가 n 인 경우는 따로 구해서 더해줄 것
    print((N - (min_num+1))*(max_num-1 - N) + N - (min_num+1) + max_num-1 - N)