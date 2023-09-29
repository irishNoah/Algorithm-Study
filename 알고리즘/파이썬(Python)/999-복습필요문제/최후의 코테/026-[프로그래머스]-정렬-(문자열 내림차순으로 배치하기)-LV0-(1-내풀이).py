'''
026-[프로그래머스]-정렬-(문자열 내림차순으로 배치하기)-LV0-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/12917

### 설계 1분, 총 2분

'''

def solution(s):
    return "".join(sorted(s, reverse=True))