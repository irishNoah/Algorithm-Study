'''
036-[프로그래머스]-자료구조-(타겟-넘버)-LV2-복습필요(1-참고).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/43165

### 참고
> 다른 사람의 풀이

??:??~??:??
### 설계 ??분, 총 ??분

'''

from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    # print(l)
    s = list(map(sum, product(*l)))
    # print(s)
    
    return s.count(target)