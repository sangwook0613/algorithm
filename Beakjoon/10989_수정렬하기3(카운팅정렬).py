### 기존에 알던 카운팅 정렬 ###
N = int(input())
numbers = [0] * N
max_num = 0
for i in range(N):
    numbers[i] = int(input())
    if numbers[i] > max_num:
        max_num = numbers[i]

counts = [0] * (max_num + 1)
for i in range(N):
    counts[numbers[i]] += 1
for i in range(1, len(counts)):
    counts[i] += counts[i-1]

result = [0] * N
for i in range(len(numbers)):
    result[counts[numbers[i]]-1] = numbers[i]
    counts[numbers[i]] -= 1

for i in range(len(result)):
    print(result[i])


### 메모리 최소화해서 처리하기 ###
import sys

# input() 보다 빠른 sys.stdin.readline() 사용
N = int(sys.stdin.readline())
counts = [0] * 10001
for i in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

# print() 보다 빠른 sys.stdout.write()
# 단, write는 str을 출력하기에 str으로 변환해서 출력해야한다.
for i in range(10001):
    if counts[i] != 0:
        for j in range(counts[i]):
            sys.stdout.write(str(i)+'\n')