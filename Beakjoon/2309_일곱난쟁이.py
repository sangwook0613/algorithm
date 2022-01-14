# 백준 2309 일곱 난쟁이
## 조합 문제이나 입력 값이 적기에 for문으로 풀이
tiny = [int(input()) for _ in range(9)]
tiny.sort()
chk = [1]*9
total = sum(tiny)
break_check = False

for i in range(9):
    chk[i] = 0
    total -= tiny[i]
    for j in range(i+1, 9):
        if total - tiny[j] == 100:
            break_check = True
            chk[j] = 0
            break
    if break_check:
        break
    chk[i] = 1
    total += tiny[i]

for i in range(9):
    if chk[i]:
        print(tiny[i])