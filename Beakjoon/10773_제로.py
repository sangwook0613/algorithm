K = int(input())
money = []

for k in range(K):
    n = int(input())
    if n != 0:
        money += [n]
    else:
        money.pop()

total = 0
if len(money) > 0:
    for i in range(len(money)):
        total += money[i]
print(total)