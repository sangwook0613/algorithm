n = int(input())
room = []
for i in range(n):
    room += list(map(str, input().split()))

row = 0
col = 0
for i in range(n):
    row_check = 0
    col_check = 0
    for j in range(n-1):
        if room[i][j] == '.' and room[i][j] == room[i][j+1] and row_check == 0:
            row += 1
            row_check = 1
        if room[i][j] == 'X':
            row_check = 0
    for j in range(n-1):
        if room[j][i] == '.' and room[j][i] == room[j+1][i] and col_check == 0:
            col += 1
            col_check = 1
        if room[j][i] == 'X':
            col_check = 0

print(row, col)