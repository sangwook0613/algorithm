# 백준 1072 게임
## 부동소수점 오차를 정확히 잡아야 풀 수 있는 문제!
## 단순히 나누지 말고 부동소수점 오차는 항상 생각하자!!
## 이분탐색을 사용하지 않는 풀이
X, Y = map(int, input().split())
z = 100 * Y // X
a = (z+1)*X - 100*Y
b = 99-z

if z >= 99:
    print(-1)
else:
    if a % b != 0:
        print(a//b + 1)
    else:
        print(a//b)

## 이분탐색을 사용하는 풀이
X, Y = map(int, input().split())
z = 100 * Y // X

if z >= 99:
    print(-1)
else:
    ans = 0
    left = 0
    right = X

    while left <= right:
        mid = (left + right) // 2
        if 100 * (Y + mid) // (X + mid) <= z:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1

    print(ans)