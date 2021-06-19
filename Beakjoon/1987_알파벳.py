dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(a, b, cnt):
    global ans
    ans = max(ans, cnt)
    for dx, dy in dxy:
        x = a + dx
        y = b + dy
        if 0 <= x < R and 0 <= y < C and not chk[ord(words[x][y]) - ord('A')]:
            chk[ord(words[x][y]) - ord('A')] = 1
            dfs(x, y, cnt+1)
            chk[ord(words[x][y]) - ord('A')] = 0


R, C = map(int, input().split())
words = [input() for _ in range(R)]

chk = [0]*(ord('Z') - ord('A') + 1)
chk[ord(words[0][0]) - ord('A')] = 1
ans = 0
dfs(0, 0, 1)
print(ans)