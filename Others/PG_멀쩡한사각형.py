# 프로그래머스 멀쩡한 사각형
## 유클리드 호제법

def solution(w, h):
    tw = w
    th = h
    # 반복문이 끝나면 tw, th 의 값는 최대공약수
    while tw != th:
        if tw > th:
            tw -= th  # tw 는 th로 나눈 나머지
        else:
            th -= tw  # th 는 tw로 나눈 나머지

    return w * h - (w + h - tw)