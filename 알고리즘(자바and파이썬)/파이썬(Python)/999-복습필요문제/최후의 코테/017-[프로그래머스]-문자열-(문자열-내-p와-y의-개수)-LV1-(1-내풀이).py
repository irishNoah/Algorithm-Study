'''
017-[프로그래머스]-문자열-(문자열-내-p와-y의-개수)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/12916

### 설계 1분, 총 3분

'''

def solution(s):
    s = s.upper()
    
    cntP = s.count('P')
    cntY = s.count('Y')
    
    if cntP == cntY:
        return True
    
    else:
        return False