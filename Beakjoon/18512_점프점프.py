# 백준 18512 점프 점프
## 너무 어렵게 생각한 문제
## 입력이 애초에 100까지 밖에 안들어오기에 100번만 해보면 다 확인할 수 있다!
X, Y, p1, p2 = map(int, input().split())
a = b = 1
ans = -1
while a < 101 and b < 101:
    if p1 == p2:
        ans = p1
        break
    elif p1 < p2:
        p1 += X
        a += 1
    else:
        p2 += Y
        b += 1

print(ans)