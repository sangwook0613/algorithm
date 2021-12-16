# 백준 15270 친구 팰린드롬
## 처음 DP로 풀려고 했느나 잘못 생각
## N과 M의 크기가 작기에 재귀로 풀이
## 코드가 깔끔하지는 않다...
def solve(idx, k, visited, chk):
    global ans
    ans = max(ans, k)
    if idx == M:
        return
    chk[idx] = 1
    solve(idx+1, k, visited, chk)
    chk[idx] = 0
    if chk[idx] == 0 and visited[num[friends[idx][0]]] == 0 and visited[num[friends[idx][1]]] == 0:
        visited[num[friends[idx][0]]] = 1
        visited[num[friends[idx][1]]] = 1
        chk[idx] = 1
        solve(idx + 1, k + 2, visited, chk)
        visited[num[friends[idx][0]]] = 0
        visited[num[friends[idx][1]]] = 0
        chk[idx] = 0


N, M = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(M)]
temp = set()
for f1, f2 in friends:
    temp.add(f1)
    temp.add(f2)
num = {n : idx for idx, n in enumerate(list(temp))}
cnt = 0
ans = 0
new_chk = [0]*M

for a in range(M):
    new_chk[a] = 1
    solve(a, 0, [0]*N, new_chk)
    new_chk[a] = 0

if N % 2 or M == 0 or ans < N:
    print(ans + 1)
else:
    print(ans)