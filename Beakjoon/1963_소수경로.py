# 1963 소수 경로
## BFS와 에라토스테네스의 체
## 초기화 잘하는 연습!! 제발!!


def bfs(num):
    q = [(num, 0)]
    visited[int(num)] = 1
    while q:
        word, cnt = q.pop(0)
        if int(word) == end:
            return cnt

        for a in range(4):
            # 첫번째 자리
            if a == 0:
                for b in range(1, 10):
                    temp = int(word[:a] + str(b) + word[a + 1:])
                    if chk_numbers[temp] and not visited[temp]:
                        visited[temp] = 1
                        q.append((str(temp), cnt+1))
            # 나머지
            else:
                for b in range(10):
                    temp = int(word[:a] + str(b) + word[a + 1:])
                    if chk_numbers[temp] and not visited[temp]:
                        visited[temp] = 1
                        q.append((str(temp), cnt+1))

    return 'Impossible'


chk_numbers = [1]*10000
visited = [0]*10000
for i in range(2,10000):
    if chk_numbers[i]:
        for j in range(i*2, 10000, i):
            chk_numbers[j] = 0

N = int(input())
for n in range(N):
    visited = [0]*10000
    start, end = map(int, input().split())
    chk_numbers[end] = 10000
    print(bfs(str(start)))
