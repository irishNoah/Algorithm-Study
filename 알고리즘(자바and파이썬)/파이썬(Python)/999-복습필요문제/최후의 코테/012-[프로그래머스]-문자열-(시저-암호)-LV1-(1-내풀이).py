'''
012-[프로그래머스]-문자열-(시저-암호)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/12926

### 설계 7분, 총 17분

'''

def solution(s, n):
    s = list(s)
    ans = []
    
    for val in s:
        if val == ' ':
            ans.append(val)
        
        elif 65 <= ord(val) <= 90:  # 대문자 범위
            alp = ord(val) + n
            if alp > 90: # Z 범위 침범 시
                alp = alp-26
            
            val = chr(alp)
            ans.append(val)
        
        elif (97 <= ord(val) <= 122): # 소문자 범위
            alp = ord(val) + n
            if alp > 122: # z 범위 침범 시
                alp = alp-26
            
            val = chr(alp)
            ans.append(val)
            
    return "".join(ans)      
    