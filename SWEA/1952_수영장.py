def dfs(start, total):
    global ans
    if start > 12:
        ans = min(ans, total)
        return
    dfs(start+1, total+(price[0]*months[start-1])) # 1일권
    dfs(start+1, total+price[1]) # 1달권
    dfs(start+3, total+price[2]) # 3달권


T = int(input())

for t in range(1, T+1):
    price = list(map(int, input().split()))
    months = list(map(int, input().split()))
    total = [0] * 16
    ans = price[3]
    dfs(1, 0)

    print('#%d %d' % (t, ans))