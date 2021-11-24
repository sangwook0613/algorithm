# 백준 17298 오큰수
# 스택을 활용하면 될것 같은데...
N = int(input())
numbers = list(map(int, input().split()))
numbers.reverse()
biggest = []

for i in range(N):
    arr = numbers[:N-i]
    num = arr.pop()
    temp = -1
    while temp < num and arr:
        temp = arr.pop()
    if temp <= num:
        temp = -1
    biggest.append(str(temp))

print(' '.join(biggest))