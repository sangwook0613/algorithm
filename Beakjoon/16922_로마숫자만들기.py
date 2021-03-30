base_num = [1, 5, 10, 50]
result = []


def solve(total, cnt, k, n):
    if cnt == n:
        global result
        if total not in result:
            result.append(total)
        return
    for i in range(k, 4):
        solve(total + base_num[i], cnt+1, i, n)


N = int(input())
solve(0, 0, 0, N)
print(len(result))