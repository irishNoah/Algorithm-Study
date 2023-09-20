'''
005-[프로그래머스]-해시-(없는-숫자-더하기)-LV1-(1-내풀이).py

- https://school.programmers.co.kr/learn/courses/30/lessons/86051
'''
def solution(numbers):
    # answer = -1
    
    answer = sum(list(set([0,1,2,3,4,5,6,7,8,9]) - set(numbers)))
    
    
    return answer