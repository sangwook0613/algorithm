def merge_sort(words):
    if len(words) == 1:
        return words
    mid_idx = len(words) // 2
    leftWords = merge_sort(words[:mid_idx])
    rightWords = merge_sort(words[mid_idx:])
    return merge(leftWords, rightWords)


def merge(leftList, rightList):
    result = []
    i = 0
    j = 0
    while i < len(leftList) and j < len(rightList):
        if leftList[i] > rightList[j]:
            result += [rightList[j]]
            j += 1
        else:
            result += [leftList[i]]
            i += 1
    if i == len(leftList):
        for a in range(j, len(rightList)):
            result += [rightList[a]]
    else:
        for a in range(i, len(leftList)):
            result += [leftList[a]]
    return result

def binary_search(findList, word, start, end):
    if start > end:
        return 0
    mid_idx = (start + end) // 2
    if word == findList[mid_idx]:
        return 1
    elif word > findList[mid_idx]:
        return binary_search(findList, word, mid_idx+1, end)
    else:
        return binary_search(findList, word, start, mid_idx-1)


A, B = map(int, input().split())
nameA = []
nameB = []
final = []
# 듣, 보 이름 명단 각각 입력 받기
for a in range(A):
    nameA += [input()]
for b in range(B):
    nameB += [input()]

nameA = merge_sort(nameA)
nameB = merge_sort(nameB)

for i in range(len(nameA)):
    word = nameA[i]
    if binary_search(nameB, word, 0, len(nameB)-1):
        final += [word]

print(len(final))
for i in range(len(final)):
    print(final[i])