# N, K = map(int, input().split())
#
# N -= 1
# start = 0
#
# while N > 0:
#     removed = (start + K - 1) % N
#     start = removed
#     print(start)
#     N -= 1
#
# print(start)
#
# # 1 2 3 4 5 6 7
# # 0 1 2 3 4 5 6
# #
# # 3 6 2 7 5 1 4
# # 2 5 1
N, K, M = map(int, input().split())

M -= 1
start = 0
ans = 1

while True:
    removed = (start + K - 1) % N
    print('start', N, start, removed, M)
    if removed == M:
        break
    if removed < M:
        M -= 1
    start = removed
    N -= 1
    print('  end', N, start, removed, M)
    ans += 1

print(ans)