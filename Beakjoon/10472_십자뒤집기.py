# 백준 10472 십자뒤집기
import sys
from collections import deque
points = [
    [0, 1, 3],
    [0, 1, 2, 4],
    [1, 2, 5],
    [0, 3, 4, 6],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
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
    while q:
        new_board, cnt = q.popleft()
        if is_same(new_board, b):
            return cnt
        for num in points:
            temp = new_board[:]
            for n in num:
                temp[n] = '.' if temp[n] == '*' else '*'
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