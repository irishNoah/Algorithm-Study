'''
029-[프로그래머스]-정렬-(K번째수)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/42748

### 참고
> 없음

### 설계 1분, 총 2분


'''

def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        step = array[i-1:j]
        step.sort()
        answer.append(step[k-1])
    
    
    return answer