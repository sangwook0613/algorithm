# 백준 1541 잃어버린 괄호
# 괄호를 하나만 치라는 말은 문제에 없다...
# 괄호를 하나면 쳐야된다고 생각하여 너무 문제를 어렵게 생각했다
# split 을 잘 활용하면 확실히 쉽다! 파이썬의 장점

formula = input().split('-')
ans = 0
before_minus = formula[0]
for i in before_minus.split('+'):
    ans += int(i)

after_minus = formula[1:]
for arr in after_minus:
    for a in arr.split('+'):
        ans -= int(a)
print(ans)