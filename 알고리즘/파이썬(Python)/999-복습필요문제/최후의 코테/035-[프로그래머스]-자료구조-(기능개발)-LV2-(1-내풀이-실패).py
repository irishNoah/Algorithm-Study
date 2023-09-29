'''
035-[프로그래머스]-자료구조-(기능개발)-LV2-(1-내풀이-실패).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/42586

### 참고
>

23:50~00:23
### 설계 20분, 총 43분
> IndexError: deque index out of range

'''
from collections import deque

def solution(progresses, speeds):
    work = []
    for i in range(len(speeds)):
        left = 100 - progresses[i]
        
        if left % speeds[i] == 0:
            work.append(left // speeds[i])
        else:
            work.append(left // speeds[i] + 1)
    print("work = ", work)    
    
    dq = deque(work)
    answer = []
    while dq:
        cmp = dq.popleft()
        cnt = 0
        
        while True:
            if cmp > dq[0]:
                dq.popleft()
                cnt += 1
            else:
                answer.append(cnt)
                break
        
    return answer