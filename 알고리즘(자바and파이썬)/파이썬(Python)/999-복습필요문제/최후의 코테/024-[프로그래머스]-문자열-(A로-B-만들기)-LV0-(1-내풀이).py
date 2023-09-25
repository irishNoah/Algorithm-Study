'''
024-[프로그래머스]-문자열-(A로-B-만들기)-LV0-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/120886

### 설계 1분, 총 2분

'''

def solution(before, after):
    if sorted(list(before)) == sorted(list(after)):
        return 1
    else:
        return 0