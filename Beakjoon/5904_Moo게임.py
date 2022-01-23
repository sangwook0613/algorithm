# 백준 5904 Moo 게임
## 분할과 정복을 활용해서 풀어야 하는문제
## 분할해서 계속 찾아나가는 과정을 간단하게 표현할 수 있는 방법을 찾아보자!
N = int(input())
count = [3]
curr = count[0]
while curr < N:
    count.append(curr*2 + len(count) + 3)
    curr = count[-1]
print(count)

