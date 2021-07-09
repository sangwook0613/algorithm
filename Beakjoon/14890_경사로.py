# 구현 문제
## 너무 어렵게 생각할 필요없다!!

def solve(arr, minL):
    down_chk = 0
    current = arr[0]
    current_length = 1

    for i in range(1, len(arr)):
        if abs(arr[i] - current) > 1:
            return 0
        if arr[i] == current:
            current_length += 1
            if down_chk and current_length >= minL:
                down_chk = 0
                current_length -= minL
        elif arr[i] > current:
            if current_length < minL or down_chk:
                return 0
            current_length = 1
            current = arr[i]
        else:
            if down_chk and current_length < minL:
                return 0
            down_chk = 1
            current_length = 1
            current = arr[i]

    if down_chk and current_length < minL:
        return 0
    return 1


N, L = map(int, input().split())

rows = [list(map(int, input().split())) for _ in range(N)]
cols = []

for i in range(N):
    temp = []
    for j in range(N):
        temp.append(rows[j][i])
    cols.append(temp)

ans = 0
for row in rows:
    ans += solve(row, L)

for col in cols:
    ans += solve(col, L)
print(ans)