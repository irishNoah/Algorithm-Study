'''
028-[프로그래머스]-자료구조-(괄호-회전하기)-LV2-(1-참고).py

### 주소
>https://school.programmers.co.kr/learn/courses/30/lessons/76502

### 참고
> https://foameraserblue.tistory.com/87

### 설계 7분, 총 37분


'''

def solution(s):
    answer = 0
    temp = list(s)
    
    for _ in range(len(s)):
 
        st = []
        for i in range(len(temp)):
            if len(st) > 0:
                if st[-1] == '[' and temp[i] == ']':
                    st.pop()
                elif st[-1] == '(' and temp[i] == ')':
                    st.pop()
                elif st[-1] == '{' and temp[i] == '}':
                    st.pop()
                else:
                    st.append(temp[i])
            else:
                st.append(temp[i])
        if len(st) == 0:
            answer += 1
        temp.append(temp.pop(0))
 
    return answer