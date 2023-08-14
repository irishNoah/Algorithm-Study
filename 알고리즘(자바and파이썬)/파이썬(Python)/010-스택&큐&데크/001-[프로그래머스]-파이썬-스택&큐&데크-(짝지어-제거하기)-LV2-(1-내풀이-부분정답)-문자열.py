# [프로그래머스]-파이썬-스택&큐&데크-(짝지어-제거하기)-LV2-(1-내풀이-부분정답)-문자열.py
# https://github.com/irishNoah/Algorithm-Study

'''
### 설계
- s의 길이가 홀수라면 어차피 짝지어진 것이 많아도 답이 될 수 없으므로 0리턴
- flag = False
- cmp  = s[0]
1. while문
    - for (i는 1부터)
        - 만약, s[i] == s[i-1]
            - flag = True
            - idx = i
            - break
        - 만약, 아니라면
            - cmp = s[i] >>> 그 다음 알파벳과 짝인지 비교해줘야 하니깐!
    - 만약, flag가 True라면
        - 만약, 문자열 s의 길이가 2이다?
            - 어차피 이거에서 제거하면 더이상 할 게 없으므로
                - 1 리턴
        - 길이가 2가 아니라면 (즉, 2보다 크다면)
            - s = s[:i-1] + s[i+1:]
    - 만약, flag가 False라면
        - 짝지은 것이 없으므로 0을 리턴

'''

def solution(s):
    answer = 1

    if len(s) % 2 == 1:
        answer = 0
        return answer
    
    flag = False # 문제에서 요구하는 문자열의 조건과 동일한지 체크하기 위한 불린 변수
    # cmp = s[0]
    
    while True:
        
        if s[0] == s[1]:
            # print("11111")
            if len(s) == 2:
                flag = True
                break
            
            s = s[2:]
            # print(s)
        
        elif s[1] == s[2]:
            # print("22222")
            s = s[0] + s[3:]
            # print(s)
        
        else:
            flag = False
            break
        
    if flag == False:
        answer = 0
        return answer
    else:
        answer = 1
        return answer 