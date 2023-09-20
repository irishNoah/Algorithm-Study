'''
006-[프로그래머스]-스택&큐-(올바른괄호)-LV1-(1-내풀이).py

- https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
'''


def solution(s):
    
    s = list(s)
    st = [s[0]]
    
    for idx in range(1, len(s)):
        
        if len(st) == 0:
            st.append(s[idx])
            continue
        
        if st[-1] == "(":
            if s[idx] == "(":
                st.append(s[idx])
            else:
                st.pop()
        
        else:
            return False
    
    # s의 마지막 요소가 "(" 일 경우에 대비
    if len(st) == 0:
        return True
    else:
        return False