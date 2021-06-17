def solve(idx, cnt, ans):
    if cnt == L:
        # 자음 모음 수 확인하는 반복문
        cnt_vowel = 0
        cnt_else = 0
        for k, w in enumerate(words):
            if w in ans:
                if chk_vowel[k]:
                    cnt_vowel += 1
                else:
                    cnt_else += 1
        if cnt_vowel >= 1 and cnt_else >= 2:
            print(''.join(ans))
        return

    for i in range(idx, C):
        if not visited[i]:
            visited[i] = 1
            ans.append(words[i])
            solve(i+1, cnt + 1, ans)
            ans.pop()
            visited[i] = 0


L, C = map(int, input().split())

words = input().split()
words.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
chk_vowel = []
for w in words:
    if w in vowel:
        chk_vowel.append(1)
    else:
        chk_vowel.append(0)

visited = [0]*C
solve(0, 0, [])