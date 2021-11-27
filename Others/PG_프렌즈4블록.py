# 프로그래머스 프렌즈4블록
# 구현 문제 - 문자열을 리스트로 변환하여 쉽게 풀 수 있었다.
def solution(m, n, board):
    new_board = []
    for i in range(m):
        new_board.append(list(board[i]))
        
    answer = 0
    while True:
        visited = []
        erase = 0
        for a in range(m):
            chk = []
            for b in range(n):
                chk.append(-1) if new_board[a][b] == ' ' else chk.append(0)
            visited.append(chk)
            
        for a in range(m-1):
            for b in range(n-1):
                if visited[a][b] >= 0:
                    word = new_board[a][b]
                    if (new_board[a+1][b] == word) and (new_board[a][b+1] == word) and (new_board[a+1][b+1] == word):
                        erase += 1
                        visited[a][b] = 1
                        visited[a+1][b] = 1
                        visited[a][b+1] = 1
                        visited[a+1][b+1] = 1
                        
        if not erase:
            break
            
        temp_board = [[] for _ in range(m)]
        for b in range(n):
            num = m-1
            for a in range(m-1, -1, -1):
                if visited[a][b] == 1:
                    pass
                else:
                    temp_board[num].append(new_board[a][b])
                    num -= 1
            for k in range(num+1):
                temp_board[k].append(' ')
        
        new_board = temp_board
    
    for row in new_board:
        for c in row:
            if c == ' ':
                answer += 1
    return answer