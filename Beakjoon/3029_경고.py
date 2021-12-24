# 백준 3029 경고
## 문제를 잘 읽자...
## 적어도 1초를 기다리며, 많아야 24시간을 기다린다.
curr = list(map(int, input().split(':')))
fin = list(map(int, input().split(':')))

if curr[2] > fin[2]:
    fin[1] -= 1
    fin[2] += 60

if curr[1] > fin[1]:
    fin[0] -= 1
    fin[1] += 60

if curr[0] > fin[0]:
    fin[0] += 24

ans = ''
chk = 0
for i in range(3):
    if i:
        ans += ':'
    temp = fin[i]-curr[i]
    if temp == 0:
        chk += 1
    if temp < 10:
        ans += ('0' + str(temp))
    else:
        ans += str(temp)

if chk == 3:
    print('24:00:00')
else:
    print(ans)