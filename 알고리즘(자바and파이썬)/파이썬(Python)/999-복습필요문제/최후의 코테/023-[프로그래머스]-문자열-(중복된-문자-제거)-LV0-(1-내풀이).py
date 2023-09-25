'''
023-[프로그래머스]-문자열-(중복된-문자-제거)-LV0-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/120888

### 설계 1분, 총 2분

'''

def solution(my_string):
    
    s = list(my_string)
    arr = []
    
    for val in s:
        if val not in arr:
            arr.append(val)
    
    return "".join(arr)