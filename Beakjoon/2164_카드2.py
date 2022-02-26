# 백준 2164 카드2
## deque 를 사용하지 않는 풀이
## 짝수 인덱스(0, 2, 4 ...)에 있는 수들만 항상 빠지는 것이기에 for 문을 활용하여 한번빼서 새로운 배열로 대체
N = int(input())
numbers = [i for i in range(1, N+1)]
k = N
while k > 1:
    new_numbers = []
    for i in range(k):
        if i % 2:
            new_numbers.append(numbers[i])
    if k % 2:
        new_numbers.append(new_numbers.pop(0))
    k = len(new_numbers)
    numbers = new_numbers

print(numbers[0])

# deque 를 사용하면 아래와 같이 간단하게 구현할 수 있다.
from collections import deque

N = int(input())
numbers = deque([i for i in range(1, N+1)])
while len(numbers) > 1:
    numbers.popleft()
    numbers.append(numbers.popleft())
print(numbers[0])