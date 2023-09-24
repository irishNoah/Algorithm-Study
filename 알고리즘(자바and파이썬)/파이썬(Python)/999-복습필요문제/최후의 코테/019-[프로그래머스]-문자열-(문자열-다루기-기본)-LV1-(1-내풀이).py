'''
019-[프로그래머스]-문자열-(문자열-다루기-기본)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/81301

### 설계 1분, 총 3분

'''

def solution(s):
    if s.isdigit() == True and len(s) in [4,6]:
        return True
    else:
        return False