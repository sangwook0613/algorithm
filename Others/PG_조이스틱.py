# 프로그래머스 조이스틱
# 그리디 하게 푼다!
def solution(name):
    numbers = [min(ord('Z')+1-ord(n), ord(n)-ord('A')) for n in name]
    answer = sum(numbers)
    
    idx = 0
    while True:
        numbers[idx] = 0
        if sum(numbers) == 0:
            return answer
        
        left = right = 1
        while numbers[idx-left] == 0:
            left += 1
            
        while numbers[idx+right] == 0:
            right += 1
            
        answer += left if left < right else right
        idx += -left if left < right else right