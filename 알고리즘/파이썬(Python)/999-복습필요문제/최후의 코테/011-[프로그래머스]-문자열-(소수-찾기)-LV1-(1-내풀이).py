'''
011-[프로그래머스]-문자열-(소수-찾기)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/12932?language=python3

### 설계 3분, 총 5분

'''

def solution(n):
    n = str(n)
    ans = list(map(int, n))
    return ans[::-1]