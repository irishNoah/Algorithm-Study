'''
014-[프로그래머스]-문자열-(3진법-뒤집기)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/68935

### 설계 8분, 총 11분

'''

def solution(n):

    arr = [] # 앞뒤 반전 3진법을 구하기 위한 리스트
    
    while n != 0:
        
        # 3을 나눈 나머지를 arr에 할당
        mod = n % 3 
        arr.append(mod)
        
        # 그 다음 몫을 구한다. 
        n = n // 3
    
    val = "".join(map(str, arr))
    answer = int(val, 3) # 구한 3진법을 10진법으로 표현
    
    return answer