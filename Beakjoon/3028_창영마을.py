# 백준 3028 창영마을
order = input()
ball = [1, 0, 0]

for a in order:
    if a == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif a == 'B':
        ball[1], ball[2] = ball[2], ball[1]
    else:
        ball[2], ball[0] = ball[0], ball[2]

for i in range(3):
    if ball[i]:
        print(i+1)
        break