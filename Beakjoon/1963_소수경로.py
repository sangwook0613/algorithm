def bfs(num):
    q = [(num, 0)]
    visited[num] = 1
    ans = 100000
    while q:
        word, cnt = q.pop(0)
        if int(word) == end:
            ans = min(cnt + 1, ans)
            continue
        # 첫번째 자리
        for b in range(1, 10):
            temp = str(b) + word[1:]
            if chk_numbers[int(temp)]:
                q.append((temp, cnt+1))
        # 두번째 자리
        for b in range(10):
            temp = word[0] + str(b) + word[2:]
            if chk_numbers[int(temp)]:
                q.append((temp, cnt+1))
        # 세번째 자리
        for b in range(10):
            temp = word[:2] + str(b) + word[3]
            if chk_numbers[int(temp)]:
                q.append((temp, cnt + 1))
        # 마지막 자리
        for b in range(10):
            temp = word[:3] + str(b)
            if chk_numbers[int(temp)]:
                q.append((temp, cnt + 1))

    return ans


chk_numbers = [1]*10000
prime_numbers = []
visited = [0]*10000
for i in range(2,10000):
    if chk_numbers[i]:
        prime_numbers.append(i)
        for j in range(i*2, 10000, i):
            chk_numbers[j] = 0


N = int(input())
for n in range(N):
    start, end = map(int, input().split())
    chk_numbers[end] = 10000
