# 프로그래머스 방문 길이
dxy = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

def solution(dirs):
    board = [[[] for _ in range(11)] for _ in range(11)]
    answer = 0
    a = b = 5
    for d in dirs:
        x = a + dxy[d][0]
        y = b + dxy[d][1]
        if 0 <= x <= 10 and 0 <= y <= 10:
            if (a, b) not in board[x][y] and (x, y) not in board[a][b]:
                answer += 1
            board[x][y].append((a, b))
            board[a][b].append((x, y))
            a = x
            b = y
        
    return answer


# 다른 풀이
# set을 활용
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2