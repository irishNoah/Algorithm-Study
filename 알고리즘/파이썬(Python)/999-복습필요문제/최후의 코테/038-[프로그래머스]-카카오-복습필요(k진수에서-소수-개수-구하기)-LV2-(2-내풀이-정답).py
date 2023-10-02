'''
038-[프로그래머스]-카카오-(k진수에서-소수-개수-구하기)-LV2-(2-내풀이-정답).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/92335

### 참고
> 다른 사람의 풀이

15:13~:15:25
### 설계 4분, 총 12분
> 주어진 n을 주어진 k에 맞게 k진수로 변환한다.
> 구한 k진수를 "0"을 기점으로 구분한다. >>> arr에 담는다.
    - 프린트
> arr에서 "1"을 제외하고 나머지 수를 에라토스테네스의 체를 활용해 소수인지 구한다.
    - 에라토스테네스의 체 >>> int(val ** 0.5)
    - 소수일 경우 answer의 값을 1 증가한다.

'''

def solution(n, k):
    s = "" # k진수를 구할 문자열
    while n != 0:
        mod = n % k
        n = n // k
        s += str(mod)
    
    s = s[::-1] # k진수 구하기
    # print("s = ", s)
    
    s = list(s.split('0'))
    # print("list s= ", s)
    
    answer = 0
    ### 에라토스테네스의 체를 활용하여 소수인지 판별
    for val in s:
        if val == '1' or val == '':
            continue
        
        val = int(val)
        flag = True # val의 소수 여부 확인
        for idx in range(2, int(val ** 0.5) + 1):
            if val % idx == 0:
                flag = False
                break
            
        if flag == True:
            answer += 1
      
    return answer