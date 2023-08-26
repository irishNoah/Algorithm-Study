# [프로그래머스]-파이썬-스택&큐&데크-(짝지어-제거하기)-LV2-(2-내풀이-정답)-스택.py
# https://github.com/irishNoah/Algorithm-Study

'''
### 설계


'''

def solution(s):

    st = [s[0]]
    
        
    for i in range(1, len(s)):
        if len(st) == 0:
            st.append(s[i])
            continue
        if st[-1] == s[i]:
            st.pop()
        else:
            st.append(s[i])
                
    
    if len(st) == 0:
        return 1
    else:
        return 0