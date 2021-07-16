def chkPalindrome(num):
    for k in range(len(num)//2 + 1):
        if num[k] != num[len(num)-k-1]:
            return False
    return True


MAX_NUM = 1003002
N = int(input())
numbers = []
chk = [1]*MAX_NUM

cnt = 0
idx = 2
ans = 0
while ans < N:
    if chk[idx]:
        for i in range(idx*2, MAX_NUM, idx):
            chk[i] = 0
        if chkPalindrome(str(idx)):
            cnt += 1
            ans = idx
    idx += 1

print(ans)