# 백준 10472 십자뒤집기
## 3x3 이기에 나올 수 있는 경우의 수가 2^9 이다
### 이걸 파악하는게 가장 중요했다
## 즉, 모든 경우의 수를 탐색해도 충분하며, BFS를 활용해서 탐색하여 풀었다.
## BFS에서 visited 체크는 dictonary를 활용해서 진행했다 - BFS에서 항상 체킹하는거 까먹지 말자
import sys
from collections import deque
points = [
    [0, 1, 3],
    [0, 1, 2, 4],
    [1, 2, 5],
    [0, 3, 4, 6],
    [1, 3, 4, 5, 7],
    [2, 4, 5, 8],
    [3, 6, 7],
    [4, 6, 7, 8],
    [5, 7, 8]
]

def is_same(arr1, arr2):
    for i in range(9):
        if arr1[i] != arr2[i]:
            return False
    return True

def bfs(s, b):
    q = deque([(s, 0)])
    visited = dict()
    visited[''.join(s)] = 1
    while q:
        new_board, cnt = q.popleft()
        if is_same(new_board, b):
            return cnt
        for num in points:
            temp = new_board[:]
            for n in num:
                temp[n] = '.' if temp[n] == '*' else '*'
            chk = ''.join(temp)
            if not visited.get(chk):
                visited[chk] = 1
                q.append((temp, cnt+1))
    return 0


input = sys.stdin.readline
P = int(input())
for _ in range(P):
    start = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    board = []
    for _ in range(3):
        board += list(input().strip())
    print(bfs(start, board))