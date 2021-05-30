def move(x1, y1, x2, y2, board):
    nums = [board[x1][y1]]
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    before_num = board[x1][y1]
    temp = 0
    x = x1
    y = y1
    k = 0
    while k < 4:
        a = x + dxy[k][0]
        b = y + dxy[k][1]
        if a > x2 or a < x1 or b > y2 or b < y1:
            k += 1
            continue
        temp = board[a][b]
        board[a][b] = before_num
        before_num = temp
        nums.append(temp)
        x = a
        y = b

    return board, min(nums)


def solution(rows, columns, queries):
    answer = []
    board = []
    for r in range(rows):
        temp = []
        for c in range(1, columns + 1):
            temp.append(columns * r + c)
        board.append(temp)

    for x1, y1, x2, y2 in queries:
        board, min_num = move(x1 - 1, y1 - 1, x2 - 1, y2 - 1, board)
        answer.append(min_num)

    return answer