def solve(a, b):
    cnt = 0
    while b > a:
        cnt += 1
        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        else:
            return -1
    if b == a:
        return cnt+1
    if b < a:
        return -1


end, start = map(int, input().split())
print(solve(end, start))