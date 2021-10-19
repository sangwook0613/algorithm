# 프로그래머스 크레인 인형뽑기 게임
## 스택 개념을 알면 쉽게 푸는 문제

def solution(board, moves):
    answer = 0
    box = []
    board_row = [[] for _ in range(len(board[0]))]
    for i in range(len(board[0])):
        for j in range(len(board) - 1, -1, -1):
            if board[j][i]:
                board_row[i].append(board[j][i])

    for m in moves:
        if len(board_row[m - 1]) == 0:
            continue
        num = board_row[m - 1].pop()
        last_num = box[len(box) - 1] if box else 0
        if num == last_num and last_num:
            box.pop()
            answer += 2
        else:
            box.append(num)
    return answer