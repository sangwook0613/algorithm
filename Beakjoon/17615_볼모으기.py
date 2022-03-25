# 백준 17615 볼 모으기
## 모든 경우의 수를 다 고려한 풀이
## 각 색마다 왼쪽이나 오른쪽으로 올 수 있는 경우의 수를 모두 고려
## flag 변수를 활용하여 각 끝점이 아닌 경우를 파악하여 계산
N = int(input())
balls = input()
red = 'R'
blue = 'B'
red_flag = True
blue_flag = True
red_left = 0
blue_left = 0
for i in range(N):
    if balls[i] != red:
        red_flag = False
    if balls[i] != blue:
        blue_flag = False
    if balls[i] == red and not red_flag:
        red_left += 1
    if balls[i] == blue and not blue_flag:
        blue_left += 1

red_flag = True
blue_flag = True
red_right = 0
blue_right = 0
for i in range(N-1, -1, -1):
    if balls[i] != red:
        red_flag = False
    if balls[i] != blue:
        blue_flag = False
    if balls[i] == red and not red_flag:
        red_right += 1
    if balls[i] == blue and not blue_flag:
        blue_right += 1

print(min(red_left, red_right, blue_left, blue_right))