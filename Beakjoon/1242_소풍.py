N, K, M = map(int, input().split())

M -= 1
start = 0
ans = 1

while True:
    removed = (start + K - 1) % N
    if removed == M:
        break
    if removed < M:
        M -= 1
    start = removed
    N -= 1
    ans += 1

print(ans)