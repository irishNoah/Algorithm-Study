'''
035-[프로그래머스]-자료구조-(기능개발)-LV2-복습필요(2-참고).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/42586

### 참고
> https://huidea.tistory.com/15

23:50~00:23
### 설계 20분, 총 43분

'''
def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer