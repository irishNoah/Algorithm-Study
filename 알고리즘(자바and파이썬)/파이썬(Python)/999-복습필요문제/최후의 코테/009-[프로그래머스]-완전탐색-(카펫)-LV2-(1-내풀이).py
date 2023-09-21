'''
009-[프로그래머스]-완전탐색-(카펫)-LV2-(1-내풀이).py

- https://school.programmers.co.kr/learn/courses/30/lessons/42842
- 참고
    - https://velog.io/@cbkyeong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%ED%8E%AB
'''

def solution(brown, yellow):
    for i in range(1, yellow +1):
        if (yellow % i == 0):
            yellow_row = int(yellow / i)
            yellow_col = i
            if (2 * (yellow_row + yellow_col) + 4 == brown):
                return [yellow_row +2, yellow_col+2]