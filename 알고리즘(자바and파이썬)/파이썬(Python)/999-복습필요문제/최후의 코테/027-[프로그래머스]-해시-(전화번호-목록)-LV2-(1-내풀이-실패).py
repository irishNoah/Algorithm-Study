'''
027-[프로그래머스]-해시-(전화번호-목록)-LV2-(1-내풀이-실패).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/42577

### 설계 7분, 총 25분

*** 데크를 이용하여 문제를 푼다.
> flag = True
> phone_book의 길이가 0이 될 때까지 while문을 돈다.
    1. 마지막 원소를 pop()하여 cmp 변수에 할당한다.
    2. for를 돈다.
        - 앞에서부터 차례대로 단어를 끌어온다.
        - 해당 단어의 길이가 cmp의 길이보다 같거나 작을 때만 수행
            - 해당 단어의 처음 부분이 cmp로 시작한다?
                - flag = False
                - return flag
    3. pop() 했었던 cmp 요소를 appendleft()하여 다시 추가한다.
> while문이 끝났을 때도 위에서 flag가 False가 안됐다면 어차피 flag는 True
    - return flag

'''
from collections import deque

def solution(phone_book):
    
    if len(phone_book) == 1:
        return flag
    
    flag = True
    dq = deque(phone_book)
    cnt = 0
    
    
    while cnt != len(phone_book):
        cnt += 1
        cmp = dq.pop()
        
        for val in dq:
            if len(cmp) < len(val) and val.startswith(cmp) == True:
            
                # if val.startswith(cmp) == True:
                flag = False
                return flag
        
        dq.appendleft(cmp)
        
    
    return flag