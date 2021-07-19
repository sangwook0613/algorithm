N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
totals = [[numbers[0][0], numbers[0][0]], [numbers[0][1], numbers[0][1]], [numbers[0][2], numbers[0][2]]]
next_totals = [[0, 0], [0, 0], [0, 0]]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            next_totals[j][0] = numbers[i][j] + min(totals[j][0], totals[j+1][0])
            next_totals[j][1] = numbers[i][j] + max(totals[j][1], totals[j+1][1])
        elif j == 1:
            next_totals[j][0] = numbers[i][j] + min(totals[j-1][0], totals[j][0], totals[j+1][0])
            next_totals[j][1] = numbers[i][j] + max(totals[j-1][1], totals[j][1], totals[j+1][1])
        else:
            next_totals[j][0] = numbers[i][j] + min(totals[j-1][0], totals[j][0])
            next_totals[j][1] = numbers[i][j] + max(totals[j-1][1], totals[j][1])
    for a in range(3):
        for b in range(2):
            totals[a][b] = next_totals[a][b]

max_num = max(totals[0][1], totals[1][1], totals[2][1])
min_num = min(totals[0][0], totals[1][0], totals[2][0])

print(max_num, min_num)