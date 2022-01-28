# # 백준 9081 단어 맞추기
# T = int(input())
# for _ in range(T):
#     word = input()
#     idx = len(word) - 1
#     chk = -1
#     while idx > 0:
#         for i in range(idx-1, -1, -1):
#             if word[i] < word[idx]:
#                 chk = i
#                 break
#             if word[i] == word[idx]:
#                 break
#         if chk != -1:
#             break
#         idx -= 1
#
#     if chk != -1:
#         ans = [word[a] for a in range(chk)] + [word[idx]]
#         temp = []
#         for a in range(chk, len(word)):
#             if a != idx:
#                 temp.append(word[a])
#         ans += sorted(temp)
#         print(''.join(ans))
#     else:
#         print(word)


# 백준 9081 단어 맞추기
T = int(input())
for _ in range(T):
    word = input()
    abc = []
    for w in word:
        
