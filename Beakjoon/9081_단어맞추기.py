# 백준 9081 단어 맞추기
## Next Permutation 알고리즘을 사용해야하는 문제
## 인덱스를 활용해서 순열을 순차적으로 이어나가는 문제
## 알고리즘 진행 순서
### 1. 오른쪽에서 왼쪽으로 순차적으로 보면서, 앞에 있는 수가 현재 수보다 작은 경우를 찾아 작은 수(A)의 인덱스를 저장한다.
### 2. A보다 큰 수 중 가장 오른쪽에 있는 수(B)를 찾는다.
### 3. A와 B 를 swap 한다.
### 4. 기존 A의 인덱스 뒤에 있는 수들을 뒤집어준다.
T = int(input())
for _ in range(T):
    temp = input()
    word = [w for w in temp]
    chk = -1

    # 1번
    for i in range(len(word) - 2, -1, -1):
        if word[i] < word[i+1]:
            chk = i
            break

    if chk != -1:
        min_word = 'Z'
        idx = 0
        # 2번
        for a in range(len(word)-1, chk, -1):
            if word[chk] < word[a] <= min_word:
                min_word = word[a]
                idx = a
                break
        # 3번
        word[chk], word[idx] = word[idx], word[chk]
        # 4번
        ans = word[:chk+1] + list(reversed(word[chk+1:]))
        print(''.join(ans))
    # 만약 1번의 경우에 해당하지 않는다면, 가장 마지막 순열이기에 그대로 출력한다.
    else:
        print(''.join(word))