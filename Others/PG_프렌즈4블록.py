# 프로그래머스 프렌즈4블록

dxy = [(0, 1), (1, 0), (1, 1)]

def solution(m, n, board):
    new_board = []
    for i in range(m):
        new_board.append(list(board[i]))
    print(new_board)
        
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
        print(visited)
        num = m-1
        temp_board = [[] for _ in range(m)]
        for b in range(n):
            num -= 1
            for a in range(m-1, -1, -1):
                if visited[a][b] == 1:
                    pass
                else:
                    temp_board[a].append(new_board[a][b])
                
        
    return answer