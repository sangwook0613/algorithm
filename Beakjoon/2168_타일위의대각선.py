# 백준 2168 타일 위의 대각선
# 최대공약수를 구하는 유클리드 호제법을 풀 수 있는 문제!
x, y = map(int, input().split())

tx = x
ty = y
ans = 0
while True:
    if tx % ty == 0:
        break
    else:
        temp = ty
        ty = tx % ty
        tx = temp

print(x+y-ty)
