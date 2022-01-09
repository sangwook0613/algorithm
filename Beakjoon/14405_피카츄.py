# 백준 14405 피카츄
pikachu = ['pi', 'ka', 'chu']
word = input()

wrong = True
temp = ''
for w in word:
    wrong = True
    temp += w
    if len(temp) == 2:
        if temp in pikachu:
            wrong = False
            temp = ''
    if len(temp) == 3:
        if temp in pikachu:
            wrong = False
            temp = ''
        else:
            break

print('YES' if not wrong else 'NO')