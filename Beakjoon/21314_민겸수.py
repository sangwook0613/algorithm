# 백준 21314 민겸 수
## 무조건 작은 수와 큰 수가 나올 수 밖에 없는 규칙이 정해져 있기에 그 규칙 대로 풀이
## 작은 수 - K 이전까지 M들은 무조건 하나로 묶고, K 는 하나씩만 묶어서 처리
## 큰 수 - K를 최대한 포함할 수 있는게 MK 를 구성, 마지막에 M들만 남는경우 하나씩 처리
word = input()
max_word = []
min_word = []
keep = ['', ''] # 작은 수, 큰 수

for w in word:
    if w == 'M':
        keep[0] += w
        keep[1] += w
    else:
        if keep[0] != '':
            num = 1/10
            for i in keep[0]:
                num *= 10
                num = int(num)
            min_word.append(num)
            keep[0] = ''
        min_word.append(5)
        if keep[1] != '':
            num = 1/10
            for i in keep[1]:
                num *= 10
                num = int(num)
            max_word.append(num*50)
            keep[1] = ''
            continue
        max_word.append(5)

if keep[0] != '':
    num = 1/10
    for i in keep[0]:
        num *= 10
        num = int(num)
    min_word.append(num)

# 큰 수에서 마지막에 M들만 남는경우 하나씩 처리
## MMM -> 111 (O) / 100 (X)
if keep[1] != '':
    for i in keep[1]:
        max_word.append(1)

print(''.join(map(str, max_word)))
print(''.join(map(str, min_word)))